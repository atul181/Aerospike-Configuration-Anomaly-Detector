import pickle

class HostsFinder:
  hosts=[]
  FILE='/etc/service/ascad/data/aero_config.yml'
  def getAddresses():
     f=open(HostsFinder.FILE,'r')
     text=f.read().split('\n')[1:-1]
     f.close()
     for i in range(len(text)):
         HostsFinder.hosts.append(text[i].split()[1])
     return HostsFinder.hosts

#print(HostsFinder.getAddresses())
    
