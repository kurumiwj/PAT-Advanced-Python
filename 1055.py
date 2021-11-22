def findAge(l,r,min_age,max_age):   #二分法查找年龄
    global rich
    ret_left,ret_right=l,r
    left,right,mid=l,r,int((l+r)/2)
    flag=False
    if max_age>=rich[r][1]:
        ret_right=right
    else:
        while left<right:
            if rich[mid][1]<max_age:
                left=mid+1
                mid=int((left+right)/2)
            elif rich[mid][1]>max_age:
                right=mid
                mid=int((left+right)/2)
            else:
                flag=True
                ret_right=mid
                break
        if not flag:
            ret_right=right-1
    left,right,mid=l,r,int((l+r)/2)
    flag=False
    if min_age<=rich[l][1]:
        ret_left=left
    else:
        while left<right:
            if rich[mid][1]<min_age:
                left=mid+1
                mid=int((left+right)/2)
            elif rich[mid][1]>min_age:
                right=mid
                mid=int((left+right)/2)
            else:
                flag=True
                ret_left=mid
                break
        if not flag:
            ret_left=left
    if ret_left>ret_right:  #不存在区间段年龄
        return -1
    else:
        return (ret_left,ret_right) #返回年龄区间段

n,k=map(int,input().split())
rich0=[]
rich=[]
d={}    #存储每个年龄的人数，将财富从大到小排序，由于最高输出人数为100，100名开外的直接舍弃
for i in range(n):
    name,age,wealth=input().split()
    age,wealth=int(age),int(wealth)
    rich0.append((name,age,wealth))
rich0.sort(key=lambda x:x[1])   #按年龄从小到大排
rich.append(rich0[0])
d[rich0[0][1]]=1
for i in range(1,n):
    if d.get(rich0[i][1],0)<100:
        d[rich0[i][1]]=d.get(rich0[i][1],0)+1
        rich.append(rich0[i])
    else:
        continue
n=len(rich)
for i in range(1,k+1):
    tmp=[]
    cnt=0
    num,min_age,max_age=map(int,input().split())
    t=findAge(0,n-1,min_age,max_age)
    print("Case #%d:"%i)
    if t==-1:
        print("None")
    else:
        tmp=rich[t[0]:t[1]+1]
        tmp.sort(key=lambda x:(-x[2],x[0])) #按财富从大到小，相同则按姓名字母序从小到大
        for j in range(min(num,len(tmp))):
            print("{:s} {:d} {:d}".format(tmp[j][0],tmp[j][1],tmp[j][2]))
