def isNqueen(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if j-i==abs(l[j]-l[i]) or l[i]==l[j]:
                return False
    return True

n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    l=l[1:]
    if isNqueen(l):
        print("YES")
    else:
        print("NO")