d={}
l=list(map(int,input().split()))
for i in range(l[0]):
    d[l[i+1]]=d.get(l[i+1],0)+1
flag=False
for i in range(l[0]):
    if d[l[i+1]]==1:
        flag=True
        print(l[i+1])
        break
if not flag:
    print("None")
