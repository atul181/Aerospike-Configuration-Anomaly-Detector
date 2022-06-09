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


path1=['None','Atul  Biggs Chrles 50G 70 50G    BB 50']
path2=['None','Atul Biggs Chrles 53687091200 70 53687091200 BB 50']

print(ConfigTree.cnfp(path1,path2))