from ConfigTree import ConfigTree


conf='''show namspaces
--------------
| namespaces |
--------------
|   "test"   |
|   "prac"   |
--------------
ok envbvubb 


'''

def getAllNamespaces(stdout):
    print(stdout)
    stdout=stdout.split('\n')
    stdout=stdout[4:]
    arr=[]
    for l in stdout:
        try:
          arr.append(l.split("\"")[1])
        except:
            pass
    return arr

print(getAllNamespaces(conf))