#枚举两个狼人，判断这两人说谎情况
n=int(input())
l=[]
flag=False
for i in range(n):
    l.append(int(input()))
for i in range(n):  #假设i号j号是狼人
    for j in range(i+1,n):
        wolf=[-1]*n #判断狼人数
        liar=[] #记录说谎的人数(需要判断一个好人一个狼人情况)
        wolf[i]=1
        wolf[j]=1
        for k in range(n):
            if l[k]*wolf[abs(l[k])-1]>0:    #说谎者
                liar.append(k)
        if len(liar)==2 and wolf[liar[0]]*wolf[liar[1]]<0:
            print(i+1,j+1)
            flag=True
            break
        else:
            continue
    if flag:
        break
if not flag:
    print("No Solution")
