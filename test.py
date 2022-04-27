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
        juli aunty
        bellar { name atul }
        }
      namespace pinki {}
}
'''
obj1=ConfigTree()
ConfigTree.process(text1,0,obj1)
#print(obj.children[0].children[0].children[1].data)
data=ConfigTree.genPaths(obj1.children[0])
ConfigTree.paths=[]

obj2=ConfigTree()
ConfigTree.process(text2,0,obj2)
#print(obj.children[0].children[0].children[1].data)
data2=ConfigTree.genPaths(obj2.children[0])


count=0
for path1 in data:
  for path2 in data2:
    if path1==path2:
      print(path1,'=',path2)
      count+=1
print(count)


