t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a+b>c:
        print("Case #%d: true" % (i+1))
    else:
        print("Case #%d: false" % (i+1))