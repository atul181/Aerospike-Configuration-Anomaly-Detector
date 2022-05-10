from ConfigTree import ConfigTree

fconf='''
A {
  B 9
}
B { C 8 }
'''

rconf='''
A {
  B 9
}
B { 
  C 32
 }
 D {
  }
'''

verd,froot,rroot=ConfigTree.isSame(fconf,rconf)
print(verd)
print(ConfigTree.stringify(ConfigTree.mccf3t(froot,rroot)))