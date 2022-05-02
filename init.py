"""
This script will start API server if the current node is alphabetic master.
It can also run as client to create parse trees for validation and synchronization of configs.
"""
import os
import requests
from hostfinder import HostsFinder
from ConfigTree import ConfigTree


app_start_command="python3 flask.py &"
conf_location="/etc/aerospike/aerospike.conf"

def startMaster():
    os.system(app_start_command)

def doClientWork(maddr):
    r=requests.get("http://",maddr,"/conf")
    mconf=r.text()
    sconf=open(conf_location,"r").read()
    isequal,mtree,stree=ConfigTree.isSame(mconf,sconf)
    if isequal:
        return
    msconfig=ConfigTree.makeCorrectConfig(mtree,stree)
    open(conf_location,"w").write(msconfig)

def doInterNodeTask():
    pass

addrs=HostsFinder.getAddresses()
addrs.sort()
for ad in addrs:
    if os.system("ping -c 1 ",ad)==0:
        #ad is master
        if os.uname().hostname in ad:
            #this is ad and master
            if requests.get("http://",ad,"/conf").status_code==200:
                pass
            else:
                startMaster()
        else:
            doClientWork(ad)

doInterNodeTask()             



