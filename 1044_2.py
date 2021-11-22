n,m=map(int,input().split())
l=list(map(int,input().split()))
option=[]
min_lost=999999
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=l[j]
        if sum>=m:
            if sum==m:
                min_lost=0
                option.append("{:d}-{:d}".format(i+1,j+1))
            else:
                lost=sum-m
                if lost==min_lost:
                    option.append("{:d}-{:d}".format(i+1,j+1))
                elif lost<min_lost:
                    min_lost=lost
                    option.clear()
                    option.append("{:d}-{:d}".format(i+1,j+1))
                else:
                    pass
            break
for i in option:
    print(i)
