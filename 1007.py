#测试点2,6未过
n=int(input())
l=list(map(int,input().split()))
dp=[0 for i in range(n)]
maxSum=l[0]
dp[0]=l[0]
start=0
end=0
for i in range(1,n):    #动态规划
    dp[i]=max(dp[i-1]+l[i],l[i])
    maxSum=max(dp[i],maxSum)
if maxSum>0:
    for i in range(n):
        flag=False #判断是否找到最大和
        start=i
        if dp[i]>=0:
            for j in range(i,n):
                if dp[j]==maxSum:   #找到最大和后不急着跳出，有可能后面还有，题目要求输出最长子列
                    end=j
                    flag=True
                elif flag or dp[j]<0:   #若是下一个不是最大或者出现最大和小于0的情况则要重新计数或者跳出
                    break
        else:
            continue
        if flag:
            break
    print(maxSum,l[start],l[end],end="")
elif maxSum==0:
    print(0,0,0)
else:
    print(0,l[0],l[n-1],end="")