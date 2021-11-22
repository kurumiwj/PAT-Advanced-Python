def binarySearch(left,right,x): #二分法查找大于目标的第一个数
    global l
    while left<right:
        mid=int((left+right)/2)
        if l[mid]>x:
            right=mid
        else:
            left=mid+1
    return left

n,m=map(int,input().split())
l=list(map(int,input().split()))
l.insert(0,0)
option=[]
min_lost=999999
for i in range(1,n+1):
    l[i]+=l[i-1]
print(l)
for i in range(1,n+1):
    if i<n:
        left,right=i,n
        target=l[i-1]+m  #在1-i下标的和上加上m即为目标总和
        j=binarySearch(i,n,target)
        tmp_sum=l[j]-l[i-1]
        if tmp_sum<min_lost:
            option.clear()
            option.append((i,j))
            min_lost=tmp_sum
        elif tmp_sum==min_lost:
            option.append((i,j))
    else:
        tmp_sum=l[n]-l[n-1]
        if tmp_sum<m:
            break
        else:
            if tmp_sum<min_lost:
                option.clear()
                option.append((i,j))
                min_lost=tmp_sum
            elif tmp_sum==min_lost:
                option.append((i,j))
print(option)
