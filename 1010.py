#测试点0未通过
def radixChange(s,radix):
    l=list(s)
    length=len(s)
    ret=0
    index=0
    while index<length:
        if l[index].isdigit():
            ret+=int(l[index])*radix**(length-index-1)
        else:
            ret+=(10+ord(l[index])-97)*radix**(length-index-1)
        index+=1
    return ret

n1,n2,tag,radix=input().split()
tag=int(tag)
radix=int(radix)
l=[n1,n2]
n=radixChange(l[tag-1],radix)   #目标十进制数
right=n
left=max(list(map(lambda x:int(x) if x.isdigit() else 10+ord(x)-97,l[2-tag])))  #取另一个数中最大的数
left,right=min(left,right),max(left,right)+1
tmp=0
if n1==n2:
    print(radix)
else:
    while left<right:   #二分
        mid=int((left+right)/2)
        if mid==left or mid==right:
            print("Impossible")
            break
        tmp=radixChange(l[2-tag],mid)
        if tmp==n:
            print(mid)
            break
        elif tmp>n:
            right=mid
        else:
            left=mid
    if left>=right:
        print("Impossible")
