from argparse import Namespace
from xml.sax.handler import property_declaration_handler
from django.db import DatabaseError
from ConfigTree import ConfigTree

text='''
server {
      namespace Atul {
        thik mem
        bellar { name atul }
        }
      namespace Tikku {}
      namespace pinki {}
}
'''
obj=ConfigTree()
ConfigTree.process(text,0,obj)
print(obj.children[0].children[2].data)