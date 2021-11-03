import math

def mul(a,b):
    return a*b
l=[]
n=int(input())
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        if i!=1:
            l.append(i)
        l.append(int(n/i))
l.sort()
index=0
cnt=1
max_index=0
max_cnt=1
m=l[index]
i=1
while i<len(l):
    if l[i]-l[i-1]==1:
        m*=l[i]
        if n%m==0:
            cnt+=1
            i+=1
        else:
            if cnt>max_cnt:
                max_cnt=cnt
                max_index=index
            cnt=1
            i=index
            index+=1
            if index>=len(l):
                break
            m=l[index]
            i=index+1
    else:
        if cnt>max_cnt:
            max_cnt=cnt
            max_index=index
        cnt=1
        i=index
        index+=1
        if index>=len(l):
            break
        m=l[index]
        i=index+1
print(max_cnt)
for j in range(max_cnt):
    if j!=0:
        print("*",end="")
    print(l[max_index+j],end="")