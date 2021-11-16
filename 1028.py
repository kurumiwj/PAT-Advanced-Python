def cmp(t,i):
    return (t[i-1],t[0])

n,c=map(int,input().split())
l=[]
for i in range(n):
    tmp=input().split()
    tmp[2]=int(tmp[2])
    l.append(tuple(tmp))
l.sort(key=lambda x:cmp(x,c))
for i in l:
    print(*i)
