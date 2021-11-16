n=int(input())
coupon=list(map(int,input().split()))
m=int(input())
product=list(map(int,input().split()))
coupon.sort(key=lambda x:-x if x>=0 else x)
product.sort(key=lambda x:-x if x>=0 else x)
total=0
i=0
j=0
while i<n and j<m:
    if coupon[i]*product[j]>0:
        total+=coupon[i]*product[j]
        i+=1
        j+=1
    else:
        while coupon[i]>=0: #过滤掉正数和0
            i+=1
            if i>=n:
                break
        while product[j]>=0:
            j+=1
            if j>=m:
                break
print(total,end="")
