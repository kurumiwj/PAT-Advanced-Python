class Node:
    def __init__(self,data,left=None,right=None):
        self.left=left
        self.right=right
        self.data=data

def insert(node,x):
    if node==None:
        node=Node(x)
    elif x<node.data:
        node.left=insert(node.left,x)
    else:
        node.right=insert(node.right,x)
    return node

def postTraversal(root):
    global postList
    if root!=None:
        postTraversal(root.left)
        postTraversal(root.right)
        postList.append(root.data)
    else:
        return

def postMirrorTraversal(root):
    global postMirrorList
    if root!=None:
        postMirrorTraversal(root.right)
        postMirrorTraversal(root.left)
        postMirrorList.append(root.data)
    else:
        return

def preTraversal(root):
    global preList
    if root!=None:
        preList.append(root.data)
        preTraversal(root.left)
        preTraversal(root.right)
    else:
        return

def preMirrorTraversal(root):
    global preMirrorList
    if root!=None:
        preMirrorList.append(root.data)
        preMirrorTraversal(root.right)
        preMirrorTraversal(root.left)
    else:
        return

n=int(input())
pre=list(map(int,input().split()))
root=Node(pre[0])
for i in range(1,len(pre)):
    insert(root,pre[i])
postList=[]
postMirrorList=[]
preList=[]
preMirrorList=[]
preTraversal(root)
preMirrorTraversal(root)
if preList==pre:
    print("YES")
    postTraversal(root)
    for i in range(len(postList)):
        if i!=0:
            print(" ",end="")
        print(postList[i],end="")
elif preMirrorList==pre:
    print("YES")
    postMirrorTraversal(root)
    for i in range(len(postMirrorList)):
        if i!=0:
            print(" ",end="")
        print(postMirrorList[i],end="")
else:
    print("NO",end="")
