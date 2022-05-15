from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  D 4
}

'''

rconf='''
A {
  B 9
}
A { D 3 }
'''

r1=ConfigTree()
r2=ConfigTree()
ConfigTree.process(rconf,0,r1)
ConfigTree.process(fconf,0,r2)
print(ConfigTree.gwpfs(r1,r2,includeExtra=True))
