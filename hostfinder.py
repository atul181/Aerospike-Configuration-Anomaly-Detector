import requests
import re

def getHostname(text):
    l=text.split('\n')
    l=l[4:]
    hosts=[]
    i=0
    while '</pre>' not in l[i]:
        curr=re.search("H=.*\">",l[i])
        if curr:
            name=curr.group(0)[2:-2]
            hosts.append(name)
        i+=1
    return hosts    


filename="hosts"
aturl="http://at.phonepe.nb6:8080/phonepeat/atbrowser.pl"


r=requests.get(aturl)
if r.status_code!=200:
    print(r.status_code)
    exit(0)

hosts=getHostname(r.text)
