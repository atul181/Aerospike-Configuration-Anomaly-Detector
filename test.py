text1='''
A {
        B d
        C d
}
'''
text2='''
A {
        B d
        C d
        K d
}
B {
        C k;
}

'''

from ConfigTree import ConfigTree

a,b,c=ConfigTree.isSame(text1,text2)
print(a)
if a:
        exit()
d=ConfigTree.makeCorrectConfig(b,c)
print(ConfigTree.stringify(d))