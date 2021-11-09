MAXN=502
INFINITY=9999999
def Dijk(road,start,n):
    dis[start]=0
    max_rescue[start]=rescue[start]
    total_num[start]=1
    for i in range(n):
        u=-1
        mindis=INFINITY
        for j in range(n):
            if not visit[j] and dis[j]<mindis:  #找出未访问过且所有路径当中最短的
                u=j
                mindis=dis[j]
        if u==-1:
            return
        visit[u]=True
        for j in range(n):
            if not visit[j] and road[u][j]<INFINITY and dis[u]+road[u][j]<=dis[j]:   #未访问过j点且从u到j有路且这条路使得从原点到该点距离更短
                if dis[u]+road[u][j]<dis[j]:
                    total_num[j]=total_num[u]   #有更短路径所以总路径条数取更短路径的总跳数
                    dis[j]=dis[u]+road[u][j]    #更新最短路径
                    max_rescue[j]=max_rescue[u]+rescue[j]   #最大救援队数量同步更新
                elif dis[u]+road[u][j]==dis[j]:
                    total_num[j]+=total_num[u]  #碰到路径相同则两者路径总条数相加
                    max_rescue[j]=max(max_rescue[u]+rescue[j],max_rescue[j])

n,m,c1,c2=map(int,input().split())
dis=[INFINITY]*n
rescue=list(map(int,input().split()))
max_rescue=[0]*n
total_num=[0]*n #最短路径总条数
road=[[INFINITY for i in range(MAXN)] for i in range(MAXN)]
# road=[[INFINITY]*MAXN]*MAXN  #这种写法会导致数据混乱
visit=[False]*MAXN
for i in range(m):
    city=list(map(int,input().split()))
    road[city[0]][city[1]]=city[2]
    road[city[1]][city[0]]=city[2]
Dijk(road,c1,n)
print(total_num[c2],max_rescue[c2])