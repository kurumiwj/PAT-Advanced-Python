m,n,s=map(int,input().split())
win=[]
i=1
pre=s
while i<=m:
    name=input()
    if i==s:
        win.append(name)
    elif i-pre==n:
        if name not in win:
            pre=i
            win.append(name)
        else:
            pre+=1
    i+=1
if len(win)==0:
    print("Keep going...")
else:
    for i in win:
        print(i)