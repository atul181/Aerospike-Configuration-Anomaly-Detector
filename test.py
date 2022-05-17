from ConfigTree import ConfigTree

opss=[
  [1,'A:8;B:11;C:10;E:8;F:8;G:8;H:8;I:8'],
  [2,'K:19;L:19;H:14;F:19'],
  [3,'J:7;P:40;L:41;K:43;N:50']
]

fconf='''
logging {
  file /home/atul {
    context any 8
    context B 11
    context C 10
  }

  file /tikku {
    context any 19
    context H 14
  }

  file /pinki {
    context P 40 
    context L 41
    context K 43
  }
}
'''



rroot=ConfigTree()
ConfigTree.process(fconf,0,rroot)

print(ConfigTree.cflc(rroot,ops=opss))