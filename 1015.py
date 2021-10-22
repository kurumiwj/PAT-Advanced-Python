import math
def decimalToRadix(n,d):
    sum=0
    p=0
    while n>0:
        sum+=n%d*(10**p)
        n=int(n/d)
        p+=1
    return sum

def radixToDecimal(n,d):
    sum=0
    p=0
    while n>0:
        sum+=n%10*(d**p)
        n=int(n/10)
        p+=1
    return sum

def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=int(n/10)
    return rev

def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if n%i==0:
                return False
    return True

while True:
    l=input().split(" ")
    l=list(map(int,l))
    if l[0]<0:
        break
    else:
        if isPrime(l[0]) and isPrime(radixToDecimal(reverse(decimalToRadix(l[0],l[1])),l[1])):
            print("Yes")
        else:
            print("No")
exit(0)