from ConfigTree import ConfigTree

text1='''
A {
    mesh-seed-address-port 12348
    mesh-seed-address-port 12349
    mesh-seed-address-port 1234510
    mesh-seed-address-port 1234511
    address 1111
}
'''
text2='''
A {
    mesh-seed-address-port 12345
    mesh-seed-address-port 12346
    mesh-seed-address-port 12347
    address 2222
}
'''

a,b,d=ConfigTree.isSame(text1,text2)
#print(a)
c=ConfigTree.makeCorrectConfig(b,d)
#print(ConfigTree.genPaths(c))
config=[]
ConfigTree.stringify(c,-2)
config=ConfigTree.config
print(''.join(config))
