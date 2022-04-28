from ConfigTree import ConfigTree

text1='''
a {
    b address
}
'''
text2='''

'''

a,b=ConfigTree.isSame(text1,text2)[1:]
c=ConfigTree.makeCorrectConfig(a,b)
print(ConfigTree.genPaths(c))
