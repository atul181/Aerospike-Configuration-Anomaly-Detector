from ConfigTree import ConfigTree

text1='''
A {
    address 9
    address 10
    address 11
    B d
}
A  k {
    f 5;
    n 6;
}
'''
text2='''
A {
    address 12
    address 13
    address 14
}
B {
    d
}

'''

a,b,d=ConfigTree.isSame(text1,text2)
print(a)
c=ConfigTree.makeCorrectConfig(b,d)
print(ConfigTree.genPaths(c))
