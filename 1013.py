#测试点3非零返回，测试点4运行超时。同样的方法C++完美AC
n,m,k=map(int,input().split())
highway=[[0 for x in range(n+1)] for x in range(n+1)]
visit=[False for x in range(n+1)]

def DFS(index):
    visit[index]=True
    for i in range(1,n+1):
        if not visit[i] and highway[index][i]>0:  #若未访问过该城市并且初始点与该点有公路
            DFS(i)

def DFSTraversal(lost):
    global cnt
    visit[lost]=True
    for i in range(1,n+1):
        if not visit[i]:
            DFS(i)
            cnt+=1

for i in range(m):
    city1,city2=map(int,input().split())
    highway[city1][city2]=1
    highway[city2][city1]=1
query=list(map(int,input().split()))
for i in query:
    cnt=0
    visit=[False for x in range(n+1)]
    DFSTraversal(i)
    print(cnt-1 if cnt>0 else cnt)
