from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  address 14
}
B { C 8 }
'''

rconf='''
A {
  B 9
  B 32
  B 64
  B 98
}
B { 
  C 32
 }
 D {
  }
'''

r1=ConfigTree()
r2=ConfigTree()
ConfigTree.process(rconf,0,r1)
ConfigTree.process(fconf,0,r2)
print(ConfigTree.gwpfs(r1,r2))
