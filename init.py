"""
This script will start API server if the current node is alphabetic master.
It can also run as client to create parse trees for validation and synchronization of configs.
"""
import subprocess
import os
import syslog
import requests
from hostfinder import HostsFinder
from ConfigTree import ConfigTree
import socket
import threading
import time
import base64
import json


app_start_command="python3 flaskserver.py"
conf_location="/etc/aerospike/aerospike.conf"
privatetokenfile="ptoken"
projectid=36378457
remote_conf_file_name="aerospike-stg-aerospikepp403.conf"
duration=3 #seconds


def getipaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

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
    os.system("echo Hi I am "+addrs[orig]+" and I am the Master > logs")
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
        syslog.syslog("\nMaster IP: "+getipaddr())
        syslog.syslog("\nSlave  IP: "+getipaddr())
        syslog.syslog('\n\n')
        secondSubTask()
        thirdSubTask()
        syslog.syslog('-'*10+'\n')

def secondSubTask():
    privatetoken=open(privatetokenfile,"r").read().split('\n')[0]
    ro=requests.get("https://gitlab.com/api/v4/projects/"+str(projectid)+"/repository/files/"+remote_conf_file_name+"?ref=main",headers={"PRIVATE-TOKEN":privatetoken})
    jo=json.loads(ro.text)
    remconf=base64.b64decode(jo['content']).decode("utf-8")
    verd,remtree,ftree=ConfigTree.isSame(remconf,open(conf_location,"r").read())
    if verd:
        syslog.syslog("\nRemote and local configurations: match\n")
        return
    paths=ConfigTree.gwpfs(remtree,ftree,includeExtra=True)
    if paths==[]:
        paths=ConfigTree.gwpfs(ftree,remtree,includeExtra=True)
        s=''
        for p in paths:
            s+='  '+p+'\n'
        syslog.syslog("\nremote and local configurations: unmatch\nlocal configuration has following extra parameters:\n"+s)
        return 
    for p in paths:
        s+='  '+p+'\n'
    syslog.syslog("\nremote and local configurations: unmatch\nremote config anomaly:\n"+s)
    

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
        syslog.syslog("\nfile and runtime configuration: match\n")
        return 
    paths=ConfigTree.gwpfs(rroot,froot)
    paths+=changelist
    s=''
    for p in paths:
        s+='  '+p+'\n'
    syslog.syslog('\nfile and runtime configuration: unmatch\nruntime config anomaly:\n'+s)
    sendREvent()
    
        

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
                

def sendREvent(service=None,description=None):
    pass

def doClientWork(maddr):
    try:
      r=requests.get("http://"+maddr+":81/conf")
    except requests.exceptions.ConnectionError:
        return
    mconf=r.text
    sconf=open(conf_location,"r").read()
    isequal,mtree,stree=ConfigTree.isSame(mconf,sconf)
    if isequal:
        syslog.syslog("\nmaster slave configuration: match\n")
        return
    paths=ConfigTree.gwpfs(mtree,stree,includeExtra=True)
    if paths==[]:
        paths=ConfigTree.gwpfs(stree,mtree,includeExtra=True)
        s=''
        for p in paths:
            s+='  '+p+'\n'
        syslog.syslog('\nmaster slave configuration: unmatch\nslave configuration has following extra parameters:\n'+s+'\n')
        sendREvent()
        return 
    s=''
    for p in paths:
        s+='  '+p+'\n'
    syslog.syslog('\nmaster slave configuration: unmatch\n')
    syslog.syslog('\nslave configuration anomaly:\n'+s)
    sendREvent()

addrs=HostsFinder.getAddresses()
addrs.sort()
for i in range(len(addrs)):
    if os.system("ping -c 1 "+addrs[i])==0:
        #ad is master
        if (os.uname().nodename in addrs[i]) or (getipaddr()==addrs[i]):
            startMaster(addrs,i+1)
        else:
            os.system("echo Hi I am "+getipaddr()+" and I am a Slave > logs")
            f=open(log_fpath,"a")
            syslog.syslog("\nMaster IP: "+addrs[i])
            syslog.syslog("\nSlave  IP: "+getipaddr())
            syslog.syslog("\n\n")
            doClientWork(addrs[i])
            thirdSubTask()
            syslog.syslog('-'*10+'\n')
            break

         



