subject=['A','C','M','E']   #按优先级排好
n,m=map(int,input().split())
l=[]
d={}
for i in range(n):
    t=[]
    tmp=input().split()
    t.append(tmp[0])
    t.extend(list(map(int,tmp[1:])))
    t.insert(1,sum(t[1:]))  #按优先级排好
    l.append(tuple(t))
for i in range(1,5):
    l.sort(key=lambda x:x[i],reverse=True)
    rank=1
    cnt=1
    for j in range(len(l)):
        if j>0: #记录有相同分数的情况
            if l[j][i]==l[j-1][i]:
                cnt+=1
            else:
                rank+=cnt
        if d.get(l[j][0])!=None:
            d[l[j][0]].append(rank)
        else:
            d[l[j][0]]=[rank]
for i in range(m):
    query=input()
    if query not in d:
        print("N/A")
        continue
    min_rank=min(d[query])
    for j in range(len(d[query])):
        if d[query][j]==min_rank:
            print(min_rank,subject[j])
            break
