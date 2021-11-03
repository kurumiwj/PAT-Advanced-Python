s1=list(input())    #商店卖的
s2=list(input())    #自己想买的
d1={}
d2={}
for i in s1:
    d1[i]=d1.get(i,0)+1
for i in s2:
    d2[i]=d2.get(i,0)+1
k1=d1.keys()
k2=d2.keys()
cnt=0
for i in k2:
    if d1.get(i,0)<d2[i]:
        cnt+=d2[i]-d1.get(i,0)
if cnt>0:
    print("No",cnt)
else:
    print("Yes",len(s1)-len(s2))