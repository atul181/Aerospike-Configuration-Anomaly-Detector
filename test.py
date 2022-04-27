from ConfigTree import ConfigTree

text=" server { \n name atul \n child { \n bnvmc kl \n bnkf dkdf \n } }"
obj=ConfigTree()
ConfigTree.process(text,0,obj)
print(obj.children[0].children[1].children[1].data)