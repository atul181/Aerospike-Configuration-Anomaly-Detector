"""
This script will start API server if the current node is alphabetic master.
It can also run as client to create parse trees for validation and synchronization of configs.
"""
import subprocess
import os
import requests
from hostfinder import HostsFinder
from ConfigTree import ConfigTree
import socket
import threading
import time


app_start_command="python3 flaskserver.py"
conf_location="/etc/aerospike/aerospike.conf"
log_fpath="log"
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
        secondSubTask()
        thirdSubTask()

def secondSubTask():
    pass

def thirdSubTask():
    import sys
    sys.stdout=open("plog","a")
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
    print(verd,lverd)
    if verd and lverd:
        return 
    paths=ConfigTree.gwpfs(rroot,froot)
    paths+=changelist
    f=open(log_fpath,"w")
    s=''
    for p in paths:
        s+=p+'\n'
    f.write('Runtime config difference\n'+s)
    f.close()
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
            pass
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
        return
    paths=ConfigTree.gwpfs(mtree,stree,includeExtra=True)
    f=open(log_fpath,"w")
    s=''
    for p in paths:
        s+=p+'\n'
    f.write('Peer configuration difference\n'+s)
    f.close()
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
            doClientWork(addrs[i])
            thirdSubTask()
            break

         



