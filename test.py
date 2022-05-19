from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  K 8
}
'''

rconf='''
A {
  B 9
  K 8
  B 9
  B 9
  B 9
}
'''

for _ in range(10):
    verd,rroot,froot=ConfigTree.isSame(rconf,fconf)
    print(verd)
    print(ConfigTree.gwpfs(rroot,froot))