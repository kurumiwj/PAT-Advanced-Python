d,n=input().split()
n=int(n)
cnt=1
ret=""
while cnt<n:
    ret=""
    i=0
    while i<len(d):
        start=i
        end=-1
        t=d[start]
        for j in range(start+1,len(d)):
            if d[j]!=d[start]:
                end=j
                break
        if end==-1: #最后一部分相同
            end=len(d)
        ret+=t+str(end-start)
        i=end
    d=ret
    cnt+=1
print(d)