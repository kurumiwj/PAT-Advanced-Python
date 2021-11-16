l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
n1,n2=l1[0],l2[0]
n=n1+n2
l1,l2=l1[1:],l2[1:]
l1.extend(l2)
l1=list(set(l1))
l1.sort()
if n%2==1:  #n为奇数
    print(l1[int(n/2)])
else:   #n为偶数
    print(l1[int(n/2)-1])
