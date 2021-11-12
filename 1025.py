def addRankList(l):
    l[0].append(1)
    pre=l[0]
    same=1
    for k in l[1:]:
        if k[1]==pre[1]: #分数相同累加同分人数
            same+=1
            k.append(pre[-1])
        else:   #分数不同则置same为1，更新排名情况
            k.append(pre[-1]+same)
            same=1
        pre=k

#存储格式：学号,分数,考场,考场排名,总排名
n=int(input())
member=[[] for x in range(n)]   #存储考场号
num=0
l=[]
local_rank={}   #记录局部排名，否则遍历数组会超时
for i in range(n):
    k=int(input())
    num+=k
    for j in range(k):
        tmp=input().split()
        member[i].append(list([tmp[0],int(tmp[1]),i]))
    member[i].sort(key=lambda x:x[1],reverse=True)
    addRankList(member[i])
    for j in member[i]:
        local_rank[j[0]]=j[-1]
    l=l+member[i]
l.sort(key=lambda x:(-x[1],x[0]))
addRankList(l)
print(num)
for i in l: #这里查找局部排名时最好不要遍历数组容易超时
    print(i[0],i[-1],i[-3]+1,local_rank[i[0]])
