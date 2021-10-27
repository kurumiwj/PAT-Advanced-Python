#字典会超时
m,n=map(int,input().split())
strict=[]
for i in range(n):
    l=input().split()
    strict.extend(l)
strict.sort()
print(strict[int(len(strict)/2)])