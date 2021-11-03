#这里用字典替换列表储存第一次输入的id，否则容易超时
import math

def isPrime(n):
    if n==2 or n==3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=int(input())
d={}
for i in range(n):
    id=input()
    if i==0:
        d[id]="Mystery Award"
    elif isPrime(i+1):
        d[id]="Minion"
    else:
        d[id]="Chocolate"
m=int(input())
s=set()
for i in range(m):
    id=input()
    print(id+": ",end="")
    if id not in d:
        print("Are you kidding?")
        continue
    if id not in s:
        s.add(id)
    else:
        print("Checked")
        continue
    print(d[id])
