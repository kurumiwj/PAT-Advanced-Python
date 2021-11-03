n=int(input())
l=list(map(list,input().split()))
s=set()
for i in l:
    i=list(map(int,i))
    s.add(sum(i))
l1=list(s)
l1.sort()
print(len(l1))
for i in range(len(l1)):
    if i!=0:
        print(" ",end="")
    print(l1[i],end="")