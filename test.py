from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  B 13
  D 4
}

'''

rconf='''
A {
  B 9
  D 4
}
'''

r1=ConfigTree()
r2=ConfigTree()
verd,a,b=ConfigTree.isSame(rconf,fconf)
print(verd)