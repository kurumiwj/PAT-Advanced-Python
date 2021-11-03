from decimal import *

n=int(input())
l=input().split()
sum="0.0"
for i in range(len(l)):
    count=(i+1)*(len(l)-i)
    sum=str(Decimal(sum)+Decimal(l[i])*count)
print(Decimal(sum).quantize(Decimal("0.00")))
