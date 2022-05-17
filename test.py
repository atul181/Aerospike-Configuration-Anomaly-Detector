from flask import Config
from ConfigTree import ConfigTree

opss=[
  [1,'A:8;B:11;C:10;E:8;F:8;G:8;H:8;I:8'],
  [2,'K:19;L:19;H:14;F:19']
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
}
'''



rroot=ConfigTree()
ConfigTree.process(fconf,0,rroot)

print(ConfigTree.cflc(rroot,ops=opss))