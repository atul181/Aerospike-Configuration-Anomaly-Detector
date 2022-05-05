'''
Create an object of this class with a none parent( which is by default) and call process method of this class and provide it with the created object as argument and also the text and its starting location(mostly 0).  
'''

import copy


class ConfigTree:

    paths=[]
    forbidden=[
        'node-id',
        'tls-address',
        'address',

    ]
    config=[]

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
        if '#' in data:
            flag=0
            first=data.split('#')[0]
            for i in range(len(first)):
                if first[i].isalnum():
                    flag=1
                    break
            #print(flag,data)
            if flag==0:
                ConfigTree.process(text,Cptr,father)
                return
            data=first
        node=ConfigTree(parent=father)
        node.data=data.split()
        node.data=' '.join(node.data)
        father.children.append(node)
        node.parent=father
        if hasNoChild:
          ConfigTree.process(text,Cptr,father)
          return
        nnptr,cdata=ConfigTree.getChildData(text,Cptr)
        ConfigTree.process(cdata,0,node)
        ConfigTree.process(text,nnptr,father)

    def genPaths(root):
        ConfigTree.paths=[]
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
    

    def isSame(text1,text2):
        root1=ConfigTree()
        root2=ConfigTree()
        conf1=ConfigTree.process(text1,0,root1)
        conf2=ConfigTree.process(text2,0,root2)
        path1=ConfigTree.genPaths(root1)
        ConfigTree.paths=[]
        path2=ConfigTree.genPaths(root2)
        p1count,p2count=0,0
        f1,f2=0,0
        for line1 in path1:
            flag=0
            for forb in ConfigTree.forbidden:
                if forb in ' '.join(line1[-1]):
                    f1+=1
                    flag=1
                    break
            if flag:
                continue
            for line2 in path2:
                if line1==line2:
                    #print(line1,line2)
                    p1count+=1
        for line2 in path1:
            flag=0
            for forb in ConfigTree.forbidden:
                if forb in ' '.join(line2[-1]):
                    f2+=1
                    flag=1
                    break
            if flag:
                continue
            for line1 in path2:
                if line2==line1:
                    p2count+=1
        #print(p1count,p2count)
        #print(len(path1))
        #print(f1,f2)
        if p1count==p2count and f1==f2 and (p1count+f1==len(path1)):
            return True,root1,root2
        return False,root1,root2


    def getLeafValue(root,path,fb,count,default):
        q=[root]
        i=0
        fbcount=1
        #print(path)
        #print(fb)
        #print(count)
        #print(fb,count)
        while i<len(path):
            j=0
            if len(q)==0:
                return default
            while j<len(q):
                if q[j].data==path[i]:
                    #print(fb,q[j].data)
                    if i==len(path)-1 and len(q[j].children)==0:
                        return q[j].data
                    i+=1
                    q=q[j].children
                    j=-1
                elif fb==q[j].data.split()[0] and len(q[j].children)==0 and fbcount==count:
                    #print(fb,fbcount,count)
                    return q[j].data
                elif fb==q[j].data.split()[0] and len(q[j].children)==0:
                    #print(q[j].data,fb,fbcount,count)
                    fbcount+=1
                elif j==len(q)-1:
                    return default
                else:
                  #print(q[j].data,fb,fbcount,count)
                  pass
                j+=1


    def makeCorrectConfig(root1,root2):
            '''
            first root is the head of tree of master config.
            '''
            q=[root1]
            fbparamscount=dict()
            while q:
                temp=q.pop(0)
                if len(temp.children)==0:
                    for fb in ConfigTree.forbidden:
                        if fb==temp.data.split()[0]:
                            #print(temp.data)
                            path=[]
                            node=temp
                            while node:
                                path.append(node.data)
                                node=node.parent
                            #print(path)
                            pathfb=copy.deepcopy(path)[1:]
                            pathfb.insert(0,fb)
                            pathfb[-1]=str(pathfb[-1])
                            pathfb=' '.join(pathfb)
                            #print('path',path)
                            #print(pathfb)
                            pathfbc=fbparamscount.get(pathfb,0)+1
                            #print(fbparamscount)
                            temp.data=ConfigTree.getLeafValue(root2,path[::-1],fb,pathfbc,temp.data)
                            #print(temp.data)
                            fbparamscount[pathfb]=pathfbc
                            break
                else:
                    q+=temp.children
            return root1
            
    def stringify(root):
        def _stringify(root,intent):
          if not root:
            return
          if root.data:
           #print('config',config)
           ConfigTree.config=ConfigTree.config+[' '*intent]+[root.data]
           #print(ConfigTree.config,id(ConfigTree.config))
          if len(root.children)==0:
            ConfigTree.config+=[' \n']
            return
          if root.data:
           ConfigTree.config+=[' {\n']
          for child in root.children:
            #print(child,ConfigTree.config)
            _stringify(child,intent+2)
          if root.data:
           ConfigTree.config=ConfigTree.config+[' '*intent]+['}\n']

        _stringify(root,-2)
        return ''.join(ConfigTree.config)

    

             
            


        


        