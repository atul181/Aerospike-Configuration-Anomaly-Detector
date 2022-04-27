'''
Create an object of this class with a none parent( which is by default) and call process method of this class and provide it with the created object as argument and also the text and its starting location(mostly 0).  
'''

import copy


class ConfigTree:

    paths=[]

    def __init__(self,parent=None):
        self.data=None
        self.parent=None
        self.children=[]

    def getParentData(text,ptr):
        i=ptr
        data=''
        isNotEmpty=False
        while i<len(text) and text[i]!="{" and text[i]!='\n':
            data+=text[i]
            if text[i].isalnum():
                isNotEmpty=True
            i+=1
        if i<len(text) and text[i]=='\n':
            isTerminating=True
        else:
            isTerminating=False
        return i+1,data,isNotEmpty,isTerminating

    def getChildData(text,ptr):
        i=ptr
        count=0
        data=''
        while i<len(text):
            if text[i]=='{':
                count+=1
            elif text[i]=='}':
                count-=1
            if text[i]=='}' and count==-1:
                return i+1,data
            data+=text[i]
            i+=1

        return i+1,data


    def process(text,ptr,father):
        '''
        cptr : child data is from here
        nnptr: next node data is from here
        '''
        if ptr>len(text)-1:
            return 
        Cptr,data,isNotEmpty,hasNoChild=ConfigTree.getParentData(text,ptr)
        if not isNotEmpty:
            ConfigTree.process(text,Cptr,father)
            return
        node=ConfigTree(parent=father)
        node.data=data.split()
        father.children.append(node)
        if hasNoChild:
          ConfigTree.process(text,Cptr,father)
          return
        nnptr,cdata=ConfigTree.getChildData(text,Cptr)
        ConfigTree.process(cdata,0,node)
        ConfigTree.process(text,nnptr,father)

    def genPaths(root):
        def getPaths(root,path):
            if not root:
                return 
            temp=copy.deepcopy(path)
            temp.append(root.data)
            if len(root.children)==0:
                ConfigTree.paths.append(temp)
                return 
            for child in root.children:
                getPaths(child,temp)
            del temp
        getPaths(root,[])
        return ConfigTree.paths
        