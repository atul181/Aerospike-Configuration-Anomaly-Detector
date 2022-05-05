text1='''
A {
        B d
        C d
}
This is ubuntu 4
'''
text2='''
A {
        B d
        C d
        K d
}
This is ubuntu 3
This is ubuntu 2
'''

from ConfigTree import ConfigTree

a,b,c=ConfigTree.isSame(text1,text2)
print(a)
if a:
        exit()
d=ConfigTree.makeCorrectConfig(b,c)
print(ConfigTree.stringify(d))