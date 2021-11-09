def changeTime(s):
    s=list(map(int,s.split(':')))
    return s[0]*3600+s[1]*60+s[2]

n=int(input())
l=[]
for i in range(n):
    l.append(input().split())
l.sort(key=lambda x:changeTime(x[1]))
print(l[0][0],end=" ")
l.sort(key=lambda x:-changeTime(x[2]))
print(l[0][0],end="")
