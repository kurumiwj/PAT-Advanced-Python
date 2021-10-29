a,b=input().split()
la=list(map(int,a.split(".")))
lb=list(map(int,b.split(".")))
result=[]
decimal=[10000001,17,29]
for i in range(3):
    result.append(la[i]+lb[i])
for i in range(2,0,-1):
    if result[i]>=decimal[i]:
        result[i]%=decimal[i]
        result[i-1]+=1
result=list(map(str,result))
print(".".join(result))