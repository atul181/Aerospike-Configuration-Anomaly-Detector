"""
This script will start API server if the current node is alphabetic master.
It can also run as client to create parse trees for validation and synchronization of configs.
"""
import os
import requests
from hostfinder import HostsFinder
from ConfigTree import ConfigTree
import socket


app_start_command="python3 flaskserver.py"
conf_location="aerospike.conf"

def getipaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def startMaster(addrs,i):
    while i<len(addrs):
        try:
           requests.get("http://"+addrs[i]+":81/shutdown")
        except:
            pass
        i+=1
    os.system(app_start_command)

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
    msconfig=ConfigTree.makeCorrectConfig(mtree,stree)
    f=open(conf_location,"w")
    f.write(ConfigTree.stringify(msconfig))
    f.close()

def doInterNodeTask():
    pass

addrs=HostsFinder.getAddresses()
addrs.sort()
for i in range(len(addrs)):
    if os.system("ping -c 1 "+addrs[i])==0:
        #ad is master
        if (os.uname().nodename in addrs[i]) or (getipaddr()==addrs[i]):
            startMaster(addrs,i+1)
        else:
            doClientWork(addrs[i])
            break

doInterNodeTask()             



