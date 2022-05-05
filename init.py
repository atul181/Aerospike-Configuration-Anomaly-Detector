"""
This script will start API server if the current node is alphabetic master.
It can also run as client to create parse trees for validation and synchronization of configs.
"""
import os
import requests
from hostfinder import HostsFinder
from ConfigTree import ConfigTree
import socket
import sys

pf=open("logs","w")
sys.stdout=pf

app_start_command="nohup python3 flaskserver.py"
conf_location="/etc/aerospike/aerospike.conf"

def getipaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def startMaster():
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
for ad in addrs:
    if os.system("ping -c 1 "+ad)==0:
        #ad is master
        if (os.uname().nodename in ad) or (getipaddr()==ad):
            #this is ad and master
            try:
               if requests.get("http://"+ad+":81/conf").status_code==200:
                 pass
               else:
                startMaster()
                break
            except requests.exceptions.ConnectionError:
                startMaster()
                break
        else:
            doClientWork(ad)
            break

doInterNodeTask()             

pf.close()


