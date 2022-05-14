from ConfigTree import ConfigTree

fconf='''
A {
  B 999
  B 9
  B 42
}
B { C 8 }
'''

rconf='''
A {
  B 42
  B 999
  B 9
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
