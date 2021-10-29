from functools import reduce

def change(a,b):
    return int(a)*10+int(b)

n=list(input())
while n!="0" and n!="6174":
    n=list(n)
    while len(n)<4:
        n.append("0")
    maxn=reduce(change,sorted(n,reverse=True))
    minn=reduce(change,sorted(n))
    n=maxn-minn
    print("{:04d} - {:04d} = {:04d}".format(maxn,minn,n))
    n=str(n)