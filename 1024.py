def isPalindromic(a):
    start=0
    end=len(a)-1
    while start<=end:
        if a[start]!=a[end]:
            return False
        start+=1
        end-=1
    return True

def add(a,b):
    carry=0
    i=len(a)-1
    j=len(b)-1
    ret=""
    while i>=0 and j>=0:
        tmpa=int(a[i])
        tmpb=int(b[j])
        s=tmpa+tmpb+carry
        ret+=str(s%10)
        carry=int(s/10)
        i-=1
        j-=1
    while i>=0:
        s=int(a[i])+carry
        ret+=str(s%10)
        carry=int(s/10)
        i-=1
    while j>=0:
        s=int(b[j])+carry
        ret+=str(s%10)
        carry=int(s/10)
        j-=1
    if carry>0:
        ret+=str(carry)
    return ''.join(list(reversed(ret)))

l=input().split()
n,k=l[0],int(l[1])
for i in range(k):
    if isPalindromic(n):
        print(n)
        print(i)
        break
    n_rev=''.join(list(reversed(n)))
    n=add(n,n_rev)
    if i==k-1:
        print(n)
        print(i+1)
