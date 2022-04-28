from ConfigTree import ConfigTree

text1='''
A {
   B {
      address 5;
   }
   c address 14;
   k host 9;
}
'''
text2='''
A {
    B {
      address 6;
    }
    
    k host 10;
}
C {
   address 9;
}

'''

a,b=ConfigTree.isSame(text1,text2)[1:]
c=ConfigTree.makeCorrectConfig(a,b)
print(ConfigTree.genPaths(c))