from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  B 12
  B 13
}
A { D 9 }
'''

rconf='''
A {
  B 9
  B 13
  D 9
}


'''

r1=ConfigTree()
r2=ConfigTree()
ConfigTree.process(rconf,0,r1)
ConfigTree.process(fconf,0,r2)
print(ConfigTree.gwpfs(r1,r2,includeExtra=True))
