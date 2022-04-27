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
        bellar { name tikku }
        }
      namespace pinki {}
}
'''
obj=ConfigTree()
ConfigTree.process(text2,0,obj)
#print(obj.children[0].children[0].children[1].data)
data=ConfigTree.genPaths(obj.children[0])
for i in data:
  print(i,end='\n\n')

