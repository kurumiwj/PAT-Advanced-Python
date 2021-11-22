m,n,k=map(int,input().split())
for i in range(k):
    flag=True
    stack=[]    #模拟栈
    l=list(map(int,input().split()))
    index=0 #待查找的下标
    start=1 #往栈里添加的元素，从2开始
    while index<n:
        if start<=n:
            stack.append(start)
        while len(stack)>0 and stack[-1]!=l[index]:
            start+=1
            stack.append(start)
            if len(stack)>m:    #超过栈的最大容量
                flag=False
                break
        if not flag:
            break
        else:   #未超过最大容量且栈顶等于序列index处值
            while len(stack)>0 and stack[-1]==l[index]:
                stack.pop()
                index+=1
        start+=1
    if not flag or len(stack)>0:
        print("NO")
    else:
        print("YES")
