def findCoins(l,r,m):
    global coins
    if coins[l]+coins[r]==m:
        return r
    left,right=l,r
    mid=int((left+right)/2)
    while left<right:
        if coins[l]+coins[mid]<m:
            left=mid+1
            mid=int((left+right)/2)
        elif coins[l]+coins[mid]>m:
            right=mid-1
            mid=int((left+right)/2)
        else:
            return mid
    return -1

n,m=map(int,input().split())
coins=list(map(int,input().split()))
coins=list(set(coins))
coins.sort()
flag=False
for i in range(n):
    j=findCoins(i,len(coins)-1,m)
    if j!=-1:
        flag=True
        print(coins[i],coins[j])
        break
if not flag:
    print("No Solution")
