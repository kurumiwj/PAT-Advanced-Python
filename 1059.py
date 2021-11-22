from math import *

def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=int(input())
prime_factor=set()  #记录素因子数
count={}    #记录所有素因子出现的次数
print("%d="%n,end="")
if n!=1:
    for i in range(2,int(sqrt(n))+1):
        while n%i==0 and isPrime(i):
            prime_factor.add(i)
            n/=i
            count[i]=count.get(i,0)+1
if len(prime_factor)==0:
    print(n,end="")
else:
    prime_factor=list(prime_factor)
    prime_factor.sort()
    for i in range(len(prime_factor)):
        if i!=0:
            print("*",end="")
        if count[prime_factor[i]]>1:
            print("{:d}^{:d}".format(prime_factor[i],count[prime_factor[i]]),end="")
        else:
            print("%d"%prime_factor[i],end="")

