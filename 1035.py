n=int(input())
user=[]
password=[]
confusing={'1':"@",'l':"L",'O':"o",'0':"%"}
modify=[]
cnt=0
for i in range(n):
    l=list(input().split())
    user.append(l[0])
    password.append(list(l[1]))
for i in range(n):
    flag=False
    for j in range(len(password[i])):
        if password[i][j] in confusing:
            if not flag:
                cnt+=1
                modify.append(i)
            flag=True
            password[i][j]=confusing[password[i][j]]
if cnt>0:
    print(cnt)
    for i in range(cnt):
        print(user[modify[i]],end=" ")
        print("".join(password[modify[i]]))
else:
    if n==1:
        print("There is 1 account and no account is modified")
    elif n>1:
        print("There are %d accounts and no account is modified" % n)
exit(0)