class Polynomial:
    def __init__(self,exp,coef):
        self.exp=exp
        self.coef=coef

p=[]
l1=list(map(float,input().split()))[1:]
l2=list(map(float,input().split()))[1:]
for i in range(0,len(l1),2):
    poly=Polynomial(l1[i],l1[i+1])
    p.append(poly)
for i in range(0,len(l2),2):
    poly=Polynomial(l2[i],l2[i+1])
    p.append(poly)
p.sort(key=lambda x:x.exp,reverse=True)
p2=[]
p2.append(p[0])
for i in range(1,len(p)):
    if p[i].exp==p[i-1].exp:
        p2[-1].coef+=p[i].coef
    else:
        if p2[-1].coef==0:
            p2.pop()
        p2.append(p[i])
if p2[-1].coef==0:
    p2.pop()
print(len(p2),end="")
if len(p2)!=0:
    for i in p2:
        print(" {:d} {:.1f}".format(int(i.exp),i.coef),end="")
