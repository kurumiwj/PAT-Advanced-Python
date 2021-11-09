from itertools import product

l1=input().split()
l2=input().split()
d={}
l1=zip(map(int,l1[1::2]),map(float,l1[2::2]))
l2=zip(map(int,l2[1::2]),map(float,l2[2::2]))
prod = list(map(lambda x: (x[0][0]+x[1][0], x[0][1]*x[1][1]), product(l1, l2)))
for exp,coef in prod:
    d[exp]=d.get(exp,0)+coef
l=list(filter(lambda x:x[1]!=0.0,sorted(d.items(),reverse=True)))
line=' '.join(map(lambda x:"{:d} {:.1f}".format(*x),l))
print(len(l),line)