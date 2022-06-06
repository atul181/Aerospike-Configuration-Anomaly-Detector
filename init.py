"""
This script will start API server if the current node is alphabetic master.
It can also run as client to create parse trees for validation and synchronization of configs.
"""
import subprocess
import os
import logging
import requests
from hostfinder import HostsFinder
from ConfigTree import ConfigTree
import socket
import threading
import time
from riemann_client.client import Client
from riemann_client.transport import  TCPTransport



app_start_command="python3 flaskserver.py"
conf_location="/etc/aerospike/aerospike.conf"
gitlab_remote_file_location="/var/local/aero_config"
environments=['nb6','nm5','nb1']
duration=3 #seconds
logging.basicConfig(filename="logs",filemode="a",format='%(asctime)s — %(name)s — %(levelname)s : %(message)s',level=0)


def getipaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def rsc(conf):
    #remove salt code.
    conf=conf.split('\n')
    i=0
    while i<len(conf):
        if "__CLUSTER__" in conf[i]:
            conf.pop(i)
            continue
        elif ("{{" in conf[i]) and ("}}" in conf[i]):
            conf[i]=conf[i].split("{{")[0]+' random'
        elif "{%"  in conf[i] and ('%}' in conf[i]):
            conf.pop(i)
            continue 
        i+=1
    return '\n'.join(conf)




def startMaster(addrs,i):
    orig=i-1
    while i<len(addrs):
        try:
           requests.get("http://"+addrs[i]+":81/shutdown")
        except:
            pass
        i+=1
    #start the thread
    t=threading.Thread(target=tasks)
    t.start()
    os.system(app_start_command)
    t.join()

def tasks():
    while 1:
        #os.system("echo test >> log2")
        time.sleep(duration)
        for i in range(len(addrs)):
            if os.system("ping -c 1 "+addrs[i])==0:
                if (os.uname().nodename in addrs[i]) or (getipaddr()==addrs[i]):
                    break
                else:
                    return
        logging.info("Master IP: "+getipaddr())
        logging.info("Slave  IP: "+getipaddr()+'\n\n')
        secondSubTask()
        thirdSubTask()
        logging.info('*'*30+'END OF LOG'+'*'*30)



def secondSubTask():
    clname=open(conf_location,"r").read().split("cluster-name")[1].split('\n')[0].split()[0]
    for env in environments:
        r=os.system('salt-call state.sls_id "/var/local/aero_config" aerospike.'+env+'.'+clname+'.config')
        if r==0:
            break
    
    try:
         remconf=open(gitlab_remote_file_location,"r").read()
    except:
        return 
    remconf=rsc(remconf)
    verd,remtree,ftree=ConfigTree.isSame(remconf,open(conf_location,"r").read())
    if verd:
        logging.info("Remote and local configurations: match\n")
        sendREvent(state='OK')
        return
    paths=ConfigTree.gwpfs(remtree,ftree,includeExtra=True)
    if paths==[]:
        paths=ConfigTree.gwpfs(ftree,remtree,includeExtra=True)
        s=''
        for p in paths:
            s+='  '+p+'\n'
        logging.critical("remote and local configurations: unmatch\nlocal configuration has following extra parameters:\n"+s)
        sendREvent(state="CRITICAL")
        return 
    s=''
    for p in paths:
        s+='  '+p+'\n'
    logging.critical("remote and local configurations: unmatch\nremote config has following different values:\n"+s)
    sendREvent(state="CRITICAL")
    

def thirdSubTask():
    root=ConfigTree()
    root.data=None
    netc=ConfigTree.mtfc('network')
    netc.parent=root
    secc=ConfigTree.mtfc('security')
    secc.parent=root
    serc=ConfigTree.mtfc('service')
    serc.parent=root
    xdrc=ConfigTree.mtfc('xdr')
    xdrc.parent=root
    nsa=getAllNamespaces()  #name space array
    nsta=[]
    for i in nsa:
        t=ConfigTree.mtfc("namespace",id=i)
        nsta.append(t)
        t.parent=root
    root.children=[netc,secc,xdrc,serc]+nsta
    #run time tree is complete and is present as root variable here
    rroot=root
    fconf=open(conf_location,"r").read()
    fct=ConfigTree()
    ConfigTree.process(fconf,0,fct)
    verd,froot,rroot=ConfigTree.isSame(fconf,ConfigTree.stringify(rroot),ignoreExtra=True)
    lverd,changelist=ConfigTree.cflc(froot)
    if verd and lverd:
        logging.info("file and runtime configuration: match\n")
        sendREvent(state='OK')
        return 
    paths=ConfigTree.gwpfs(rroot,froot)
    paths+=changelist
    s=''
    for p in paths:
        s+='  '+p+'\n'
    logging.critical('file and runtime configuration: unmatch\nruntime config has following different values:\n'+s)
    sendREvent(state='CRITICAL')
    
        

def getAllNamespaces():
    q=subprocess.Popen(['aql','-c',"SHOW NAMESPACES"],stdout=subprocess.PIPE)
    stdout,stderr=q.communicate()
    stdout=stdout.decode('utf-8')
    stdout=stdout.split('\n')
    stdout=stdout[4:]
    arr=[]
    for l in stdout:
        try:
           arr.append(l.split("\"")[1])
        except:
            if '-' in l:
                break
    return arr
                

def sendREvent(state,service="AScad",description="Aerospike configuration anomaly alert",ttl=60):
    server=TCPTransport(host="riemann-prod.phonepe.nb6",port=5555)
    with Client(server) as client:
       ret=client.event(service=service,description=description,state=state,ttl=ttl)
    logging.info("State of the event that was sent to Riemann: "+state+"\nResponse from Reimann Server: "+str(ret))
    
    


def doClientWork(maddr):
    try:
      r=requests.get("http://"+maddr+":81/conf")
    except requests.exceptions.ConnectionError:
        return
    mconf=r.text
    sconf=open(conf_location,"r").read()
    isequal,mtree,stree=ConfigTree.isSame(mconf,sconf)
    if isequal:
        logging.info(maddr+" and current node configuration: match\n")
        sendREvent(state='OK')
        return
    paths=ConfigTree.gwpfs(mtree,stree,includeExtra=True)
    if paths==[]:
        paths=ConfigTree.gwpfs(stree,mtree,includeExtra=True)
        s=''
        for p in paths:
            s+='  '+p+'\n'
        logging.critical(maddr+' and current node configuration: unmatch\ncurrent node configuration has following extra parameters:\n'+s+'\n')
        sendREvent(state="CRITICAL")
        return 
    s=''
    for p in paths:
        s+='  '+p+'\n'
    logging.critical(maddr+' and current node configuration: unmatch\n')
    logging.critical(maddr+' config has following different values:\n'+s)
    sendREvent(state="CRITICAL")


addrs=HostsFinder.getAddresses()
addrs.sort()
hostname=os.uname().nodename


for i in range(len(addrs)):
    if os.system("ping -c 1 "+addrs[i])==0:
        #ad is master
        if (os.uname().nodename in addrs[i]) or (getipaddr()==addrs[i]):
            startMaster(addrs,i+1)
        else:
            logging.info("Master IP: "+addrs[i])
            logging.info("Slave  IP: "+getipaddr()+'\n\n')
            doClientWork(addrs[i])
            thirdSubTask()
            logging.info('*'*30+'END OF LOG'+'*'*30)
            break

         


