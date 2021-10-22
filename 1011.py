from functools import reduce

games=3
odd=[]
bet=["W","T","L"]
bet2=[]
def mul(x,y):
    return x*y

for i in range(games):
    l=list(map(float,input().split("\n")[0].split(" ")))
    odd.append(max(l))
    bet2.append(bet[l.index(max(l))])

total=(reduce(mul,odd)*0.65-1)*2
print(*bet2,"%.2f" % total)
