MAXN=100005
next=[0]*MAXN
start1,start2,n=map(int,input().split())
# cnt=0
visited=[False]*MAXN
for i in range(n):
    tmp_index,tmp_data,tmp_next=input().split()
    next[int(tmp_index)]=int(tmp_next)
#     if tmp_next=='-1':  #统计一共有几个-1，如果有一个说明有公共后缀，否则没有公共后缀(由于只有两个字符串所以最多两个-1)
#         cnt+=1
if start1==-1 or start2==-1:    #无公共后缀或者有一个单词为空
    print("-1",end="")
else:
    start=start1
    while start!=-1:
        visited[start]=True
        start=next[start]
    start=start2
    while start!=-1:
        if visited[start]:
            break
        start=next[start]
    if start!=-1:
        print("%05d"%start,end="")
    else:
        print("-1",end="")
