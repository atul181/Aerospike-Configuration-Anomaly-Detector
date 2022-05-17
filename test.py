from flask import Config
from ConfigTree import ConfigTree

opss=[
  [1,'A:8;B:9;C:10'],
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

root=ConfigTree()
logging=ConfigTree()
st1=ConfigTree()
st2=ConfigTree()
st3=ConfigTree()
st4=ConfigTree()
st5=ConfigTree()
st6=ConfigTree()

logging.data='logging'
logging.parent=root
root.children=[logging]

st1.data="file /home/atul"
st1.parent=logging
logging.children.append(st1)


st3.data="context any 8"
st3.parent=st1
st1.children.append(st3)

st4.data="context B 9"
st4.parent=st1
st1.children.append(st4)

st5.data="context C 10"
st5.parent=st1
st1.children.append(st5)


rroot=ConfigTree()
ConfigTree.process(fconf,0,rroot)

print(ConfigTree.cflc(rroot,ops=opss))