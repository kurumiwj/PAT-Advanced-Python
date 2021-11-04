n=int(input())
l=list(map(int,input().split()))
l.sort()
pre=0 #通过与前一个数的差是否为1来找出丢失的最小数
flag=False #判断是否是第一个正整数
for i in l:
    if i>0:
        if i!=1 and not flag:
            print("1")
            break
        else:
            if not flag:
                flag=True
            else:
                if i-pre>1:
                    print(pre+1)
                    break
            pre=i
if not flag:    #都为负数或0的情况
    print("1")
elif i-pre==0:  #都是按次序排列则输出最后一个数+1的值
    print(i+1)