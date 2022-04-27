"""
This script will start API server if the current node is alphabetic master.
It can also run as client to create parse trees for validation and synchronization of configs.
"""

import requests as r
import os
import pickle

try:
  master=pickle.load(open("hosts","rb"))[0]
except:
    exit()

API="http://"+master+".phonepe.nb6/conf"
startMasterCommand="python3 flask.py &"

if master==os.uname().nodename and r.get(API).status_code!=200:
    os.system(startMasterCommand)
    exit()
elif r.get(API).status_code==200:
   exit()

rq=r.get(API)
if rq.status_code!=200:
  print("Error in connecting")
  exit(0)





