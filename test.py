from ConfigTree import ConfigTree

text1='''
server {
      namespace Atul {




        thik mem
        bellar { name atul }
        }
      namespace Tikku {}
      namespace pinki {}
}
'''
text2='''
server {
      namespace Tikku {}
      namespace Atul {
        thik mem
        bellar { name      atul }
        }
      namespace pinki {}
}
'''

print(ConfigTree.isSame(text1,text2))