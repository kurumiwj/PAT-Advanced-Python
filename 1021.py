#测试点3超时
def DFS(index,depth):
    global n
    global max_depth
    if depth>max_depth: #若当前深度超过已有的最大深度则更新最大高度且根数组清空，放入当前节点
        max_depth=depth
        root.clear()
        root.add(index)
    elif depth==max_depth:  #若当前深度等于最大深度则将该节点加入根数组中
        root.add(index)
    visit[index]=True
    for i in range(1,n+1):
        if i in graph[index] and not visit[i]:    #若index与i之间有边且i未访问过则继续向下遍历
            DFS(i,depth+1)
    return

def DFSTraversal():
    global n
    global visit
    cnt=0
    for i in range(1,n+1):  #判断连通块的个数
        if not visit[i]:
            DFS(i,1)
            cnt+=1
    return cnt

n=int(input())
max_depth=0
root=set()
visit=[False for x in range(n+1)]
graph={}
for i in range(1,n+1):
    graph[i]=[]
for i in range(n-1):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
cnt=DFSTraversal()
if cnt>1:
    print("Error: %d components" % cnt,end="")
else:   #由于题目明确说明是n个顶点n-1条边，所以当连通块的数量是1时一定不是环
    s1=root.copy()
    for i in root:
        visit=[False for x in range(n+1)]
        DFS(i,1)
        break
    s2=root.copy()
    for i in s2:
        s1.add(i)
    l=list(s1)
    l.sort()
    for i in l:
        print(i)
