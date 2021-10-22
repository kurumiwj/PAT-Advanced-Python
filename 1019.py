def decimalToRadix(n,d):
    sum=[]
    while n>0:
        sum.append(n%d)
        n=int(n/d)
    sum.reverse()
    return sum

def isPalindromic(l):
    r=list(reversed(l))
    for i in range(len(l)):
        if l[i]!=r[i]:
            return False
    return True

l=list(map(int,input().split(" ")))
dtr=decimalToRadix(l[0],l[1])
if isPalindromic(dtr):
    print("Yes")
else:
    print("No")
for i in range(len(dtr)):
    if i!=0:
        print(" ",end="")
    print(dtr[i],end="")

exit(0)