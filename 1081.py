def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

def fracSum(a1,b1,a2,b2):   #a1,a2为分子,b1,b2为分母
    g=gcd(b1,b2)
    mul1=b2/g
    mul2=b1/g
    b1=int(b1*mul1)
    a1=int(a1*mul1)
    b2=int(b2*mul2)
    a2=int(a2*mul2)
    return (a1+a2,b1)

n=int(input())
l=input().split()
l1=[]
for i in l:
    s=tuple(map(int,i.split('/')))
    l1.append(s)
a,b=l1[0][0],l1[0][1]
for i in range(1,len(l1)):
    (a,b)=fracSum(a,b,l1[i][0],l1[i][1])
g=gcd(a,b)
a=int(a/g)
b=int(b/g)
s_int=int(a/b)
s_frac=a%b
if a==0:
    print("0")
elif s_int==0:
    print("{:d}/{:d}".format(a,b))
else :
    if s_frac==0:
        print("{:d}".format(s_int))
    else:
        print("{:d} {:d}/{:d}".format(s_int,s_frac,b))
