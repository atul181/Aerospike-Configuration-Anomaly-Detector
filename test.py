from ConfigTree import ConfigTree

fconf='''
A {
  B 9
}
B { C 8 }
D {
  E 12
}
'''

rconf='''
A {
  B 9
}
B { 
  C 32
 }
 D {
  E 32
  F {
    K 99999
  }
'''

verd,froot,rroot=ConfigTree.isSame(fconf,rconf)
print(verd)
print(ConfigTree.stringify(ConfigTree.mccf3t(froot,rroot)))