from flask import Config
from ConfigTree import ConfigTree

opss=[
  [1,'A:8;B:9;C:10;E:8;F:8;G:8;H:8;I:8'],
  [2,'K:9;L:19;H:14;F:9']
]

fconf='''
logging {
  file /home/atul {
    context any 8
    context B 9
    context C 10
  }
  file /tikku {
    context K 9
    context L 19
    context H 14
  }
}
'''



rroot=ConfigTree()
ConfigTree.process(fconf,0,rroot)

print(ConfigTree.cflc(rroot,ops=opss))