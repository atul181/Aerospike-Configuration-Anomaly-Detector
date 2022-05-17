from ConfigTree import ConfigTree

fconf='''
A {
  B 9
  B 12
  B 13
}
A { D 9 }
D { n {b i }}
'''

rconf='''
A {
  B 9
  B 13
  B 12
  D 9
  P 5
  N 8
}
D {
  j 7
  f k
  n {
    b i
  }
}

'''

print(ConfigTree.isSame(fconf,rconf,ignoreExtra=True))