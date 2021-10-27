maxn=100001
l=list(map(int,input().split()))
total_distance=sum(l)-l[0]
m=int(input())
dis=[0]*maxn
for i in range(2,l[0]+1):
    dis[i]=dis[i-1]+l[i-1]
for i in range(m):
    a,b=map(int,input().split())
    start=min(a,b)
    end=max(a,b)
    d=dis[end]-dis[start]
    print(min(d,total_distance-d))