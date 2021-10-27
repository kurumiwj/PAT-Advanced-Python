st=input()
length=len(st)
n1=n3=int((length+2)/3)
n2=(length+2-n1*2)
index=0
for i in range(n1-1):
    print(st[index]+" "*(n2-2)+st[length-1-index])
    index+=1
for i in range(n2):
    print(st[index],end="")
    index+=1
