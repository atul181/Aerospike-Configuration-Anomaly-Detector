'''
Create an object of this class with a none parent( which is by default) and call process method of this class and provide it with the created object as argument and also the text and its starting location(mostly 0).  
'''

import copy
import subprocess



class ConfigTree:

    paths=[]
    forbidden=[
        'node-id',
        'tls-address',
        'address',

    ]
    dncc=[
        ''
    ]
    config=[]

    def __init__(self,parent=None):
        self.data=None
        self.parent=parent
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
        '''
        Output is a list : [[None, 'A', 'B 9'], [None, 'B', 'C 32'], [None, 'D']]
        '''
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
    

    def isSame(text1,text2,ignoreExtra=False):
        '''
        returns three values :
           1. boolean value to indicate whether both config strings are same or not.(call it verd)
           2. ConfigTree root for text1.(call it mroot)
           3. ConfigTree root for text2.(call it sroot)
        if ignoreExtra is True then:
            it will return true as value of verd even if there are some parameters in text2 that are not present in text1;given that the values of text1 parameters are all same in text2.
            it will return false in all other cases.
        else:
            will return true as value of verd only if both the texts exactly match in terms of the values of their parameters and the parameters itself.Meaning that if A is in text2 then A should also be in text1 otherwise it will return false as value of verd.
        
        '''
        root1=ConfigTree()
        root2=ConfigTree()
        ConfigTree.process(text1,0,root1)
        ConfigTree.process(text2,0,root2)
        path1=ConfigTree.genPaths(root1)
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
                    p1count+=1
                    break
                elif ignoreExtra and ConfigTree.cnfp(line1,line2):
                    p1count+=1
                    break
                elif ignoreExtra and 'logging' in line1:
                    p1count+=1
                    break
        for line2 in path2:
            flag=0
            for forb in ConfigTree.forbidden:
                if forb in ' '.join(line2[-1]):
                    f2+=1
                    flag=1
                    break
            if flag:
                continue
            for line1 in path1:
                if line1==line2:
                    p2count+=1
                    break
        #print(p1count,p2count)
        #print(len(path1))
        #print(f1,f2)
        if not ignoreExtra:
            if p1count==p2count and f1==f2 and (p1count+f1==len(path1)) and (p2count+f2==len(path2)):
               return True,root1,root2
            return False,root1,root2
        else:
            if (p1count+f1)==len(path1):
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
        ConfigTree.config=[]
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
    
    def mtfc(ctx,id=None,conf='',isConfigAvailable=False):
        # make tree from context
        # ctx is context
        #ctx is the root of tree
        if not isConfigAvailable:
            if not id:
               conf=subprocess.run(["asinfo","-v","get-config:context="+ctx,"-l"],capture_output=True).stdout.decode("utf-8")
            else:
                string='asinfo -v "get-config:context='+ctx+';id='+id+'" -l'
                conf=subprocess.check_output(string,shell=True,universal_newlines=True)
        cl=conf.split('\n')
        #print(cl)
        root=ConfigTree()
        if not id:
            root.data=ctx
        else:
            root.data=ctx+' '+id
        for l in range(len(cl)):
            if not hasalnum(cl[l]):
                continue
            params,val=cl[l].split('=')
            if ':' in val:
                val=' '.join(val.split(':'))
            params=params.split('.')
            arr=root.children
            parent=root
            i=0
            while i<len(params):
                j=0
                if len(arr)==0:
                    nn=ConfigTree(parent=parent)
                    nn.data=params[i]
                    parent.children.append(nn)
                    parent=nn
                    arr=[]
                    i+=1
                    continue
                while j<len(arr):
                    #print(arr)
                    if arr[j].data==params[i]:
                        parent=arr[j]
                        arr=arr[j].children
                        j=0
                        i+=1
                        continue
                    elif j==len(arr)-1:
                        #print(parent.data)
                        nc=ConfigTree(parent=parent)
                        nc.data=params[i]
                        #print(params[i])
                        #print(nc.parent)
                        nc.parent.children.append(nc)
                        parent=nc
                        arr=[]
                        j=0
                        i+=1
                        continue
                    j+=1
            parent.data+=' '+val
        return root 
    
    def mccf3t(froot,rroot):
        #make correct config for 3rd task
        #froot is file root and rroot is runtime root
        #returns correct root
        q=[froot]
        pathd={}
        while q:
            node=q.pop(0)
            if len(node.children):
                q+=node.children
                continue
            path=[]
            temp=node
            while node:
                path+=[node.data]
                node=node.parent
            #print(path)
            path=path[::-1]
            path[-1]=' '.join(path[-1].split()[:-1])
            #print(path)
            if pathd.get(' '.join(path[1:]),0)==0:
                pathd[' '.join(path[1:])]=0
            else:
                pathd[' '.join(path[1:])]+=1
            temp.data=ConfigTree.glv3(rroot,path,pathd[' '.join(path[1:])],temp.data)
        return froot

    def glv3(root,path,count,default):
        #get leaf value for 3rd task
        lcount=0
        i=0
        q=[root]
        while i<len(path):
            j=0
            while j<len(q):
                #print(path[i],q[j].data,count,lcount)
                #print(path[i],q[j].data)
                if path[i]==q[j].data:
                    q=q[j].children
                    j=0
                    i+=1
                    continue
                elif i==len(path)-1 and len(q[j].children)==0 and path[i] in q[j].data:
                    if q[j].data.split()[:-1]==path[i].split() and lcount==count:
                        return q[j].data
                    elif q[j].data.split()[:-1]==path[i].split()[:-1]:
                        lcount+=1
                elif j==len(q)-1:
                    return default
                j+=1
    
    def gwpfs(mroot,sroot,includeExtra=False):
        '''
        Get wrong params from slave
        mroot is master root
        sroot is slave root
        If includeExtra is true then it will get all paths that are not present in slave but in master they are present.
        returns a list of paths that have wrong values in their leafs.
        '''
        wp=[] #wrong paths
        mpcount={}
        spcount={}
        mpaths=ConfigTree.genPaths(mroot)
        spaths=ConfigTree.genPaths(sroot)
        #print(mpaths,'\n',spaths)
        for i in range(len(mpaths)):
            mpaths[i][0]='None'
            pwpol='.'.join(mpaths[i][:-1]+mpaths[i][-1].split()[:-1])
            if mpcount.get(pwpol,0)==0:
                mpcount[pwpol]=1
            else:
                mpcount[pwpol]+=1
            spcount={}
            for j in range(len(spaths)):
                spaths[j][0]='None'
                spwpol='.'.join(spaths[j][:-1]+spaths[j][-1].split()[:-1])
                if spcount.get(spwpol,0)==0:
                    spcount[spwpol]=1
                else:
                    spcount[spwpol]+=1
                #matching starts here
                if mpaths[i]==spaths[j]:
                    if spcount[spwpol]==mpcount[pwpol]:
                        break
                elif not includeExtra:
                    if ConfigTree.cnfp(spaths[j],mpaths[i]):
                        if spcount[spwpol]==mpcount[pwpol]:
                            break
                    else:
                        if pwpol.split('.')[-1] in ConfigTree.forbidden:
                            break
                        if j==len(spaths)-1 and spcount.get(pwpol,0)!=0:
                            wp.append('.'.join('.'.join(mpaths[i]).split('.')[1:]))
                            break

                else:
                    if pwpol.split('.')[-1] in ConfigTree.forbidden:
                        break
                    elif pwpol==spwpol:
                        if spcount[spwpol]==mpcount[pwpol]:
                            wp.append('.'.join('.'.join(mpaths[i]).split('.')[1:]))
                            break
                        elif j==len(spaths)-1 and includeExtra:
                            wp.append('.'.join('.'.join(mpaths[i]).split('.')[1:]))
                            break
                    elif j==len(spaths)-1 and includeExtra:
                        wp.append('.'.join('.'.join(mpaths[i]).split('.')[1:]))
                        break
        return wp
    
    def cflc(froot):
        '''
        check file log config
        This is to be used only in 3rd subtask.
        '''
        for i in range(len(froot.children)):
            if froot.children[i].data=="logging":
                lognode=froot.children[i]
                break
        i=0
        ops=[]
        while 1:
            op=subprocess.run(["asinfo","-v",'"log/'+str(i)+'"'],capture_output=True).stdout.decode("utf-8")
            if "ERROR" in op:
                break
            op=op[:-1]
            ops.append([i,op])
            i+=1

        if len(lognode.children)!=i:
            return False,["logging.*"]
        retlist=[]
        kvi=ops[0][1].split(';')
        #ref is refernce of param names
        for i in range(len(ops)):
            kv=ops[i][1].split(';')
            bin=lognode.children[i]
            flogc=list(kv)
            #file log conf
            for ch in bin.children:
                ctx,ranger,value=ch.data.split()
                #print(ctx,ranger,value)
                if ranger=="any":
                    for j in range(len(flogc)):
                        key,val=flogc[j].split(':')
                        val=value
                        flogc[j]=':'.join([key,val.upper()])
                else:
                    for j in range(len(flogc)):
                        if flogc[j].split(':')[0]==ranger:
                            key,val=flogc[j].split(':')
                            val=value
                            flogc[j]=':'.join([key,val.upper()])
            temp=ops[i][1].split(';')
            for k in range(len(flogc)):
                if flogc[k] not in temp:
                    retlist.append("logging."+lognode.children[i].data)
                    break
        if retlist==[]:
            return True,[]
        else:
            return False,retlist

    def cnfp(path1,path2):
        '''
        compare number from path
        Is ony used in case of comparing file and runtime paths.
        path1 is file path and path2 is runtime path.
        '''
        if path1[:-1]!=path2[:-1]:
            return False
        pp1,pp2=path1[-1],path2[-1] #part of path1 and part of path2
        pp1=pp1.split()
        pp2=pp2.split()
        if len(pp1)!=len(pp2):
            return False
        for i in range(len(pp1)):
            if pp1[i]==pp2[i]:
                continue
            else:
                val2=pp2[i]
                num,unit='',''
                for j in range(len(pp1[i])):
                    if pp1[i][j] in '1234567890':
                        num+=pp1[i][j]
                    else:
                        unit=pp1[i][j:]
                        break
                if num=='':
                    return False
                if unit=='G' or unit=="GiB":
                   mult=1073741824
                elif unit=='T' or unit=="TiB":
                   mult=1099511627776
                elif unit=='M' or unit=="MiB":
                   mult=1048576
                elif unit=="K" or unit=="KiB":
                   mult=1024
                else:
                   return False
                if int(num)*mult==int(val2):
                   continue
                return False
        return True
                



def hasalnum(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
    return False     
            
        