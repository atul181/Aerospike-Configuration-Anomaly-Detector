from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  B 12
  B 15
}
'''

rconf='''
A {
  B 9
  B 13
  B 12
  B 15
}
'''

verd,fr,rr=ConfigTree.isSame(fconf,rconf)
if not verd:
  print(ConfigTree.gwpfs(rr,fr))