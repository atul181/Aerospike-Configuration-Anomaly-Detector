from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  K 4G
  Z 4
  tls-name null
  C K
}
'''

rconf='''
A {
  B 9
  K 4G
  tls-name null
  Z 4
  D 9 
}
'''


verd,froot,rroot=ConfigTree.isSame(fconf,rconf)
print(verd)
print(ConfigTree.gwpfs(rroot,froot,includeExtra=True))