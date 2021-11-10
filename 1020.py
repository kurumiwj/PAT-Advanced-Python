class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def makeRoot(postOrder,inOrder):    #通过中序遍历和后序遍历确定一棵树
    if len(postOrder)==0:
        return None
    root=Node(postOrder[-1])
    root_pos=inOrder.index(root.data)
    root.left=makeRoot(postOrder[:root_pos],inOrder[:root_pos])
    root.right=makeRoot(postOrder[root_pos:-1],inOrder[root_pos+1:])
    return root
#   测试树建立是否正确
def preTraversal(root):
    print(root.data)
    if root.left!=None:
        preTraversal(root.left)
    if root.right!=None:
        preTraversal(root.right)

n=int(input())
postOrder=list(map(int,input().split()))
inOrder=list(map(int,input().split()))
root=makeRoot(postOrder,inOrder)
# preTraversal(root)
bfs=[root]
cnt=0
for i in bfs:
    cnt+=1
    print(i.data,end=(" " if cnt!=n else ""))
    if i.left!=None:
        bfs.append(i.left)
    if i.right!=None:
        bfs.append(i.right)
