import math

def isPrime(s):
    s=int(s)
    if s==2 or s==3:
        return True
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True

l,k=map(int,input().split())
num=input()
flag=False
for i in range(len(num)-k+1):
    if isPrime(num[i:i+k]):
        flag=True
        print(num[i:i+k])
        break
if not flag:
    print("404")