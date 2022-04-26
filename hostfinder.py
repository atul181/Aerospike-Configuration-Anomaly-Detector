import pickle
from subprocess import run

filen="hosts"
cmd=["ppec","search","--tags","INTERN,T3","-r","nb6"]
hosts=[]

cmdo=run(cmd,capture_output=True)
data,err=cmdo.stdout,cmdo.stderr

data=data.decode("utf-8")
data=data.split('\n')
for host in data:
    if '- ' in host:
        hosts.append(host.split('- ')[1])



f=open(filen,'wb')
pickle.dump(hosts,f)
f.close()

