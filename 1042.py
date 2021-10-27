import copy

deck=["S","H","C","D","J"]
card=[]
for j in range(5):
    if j!=4:
        for i in range(1,14):
            card.append(deck[j]+str(i))
    else:
        for i in range(1,3):
            card.append(deck[j]+str(i))
shuffle=copy.copy(card)
n=int(input())
order=list(map(int,input().split()))
for i in range(n):
    for j in range(len(order)):
        shuffle[order[j]-1]=card[j]
    card=copy.copy(shuffle)
print(*shuffle)