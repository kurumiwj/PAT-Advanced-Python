def isZero(s):  #判断字符串是否全部为0
    n=len(s)
    for i in range(n):
        if s[i]!='0' and s[i]!='.':
            return False
    return True

def findFirstValidDigit(s): #找到第一位有效数字
    index=-1
    for i in range(len(s)):
        if s[i]!='.' and s[i]!='0':
            index=i
            break
    return i

def changeForm(s,n):  #转换成标准写法
    point=s.find('.')
    ret="0."
    if isZero(s):
        ret+='0'*n+"*10^0"
    else:
        start=findFirstValidDigit(s)
        new_s=""
        index=start
        cnt=0
        while cnt<n:    #这里有效数字后面可能会含有小数点，需要处理一下
            if s[index]!='.':
                new_s+=s[index]
                cnt+=1
            index+=1
        s=s[start:]
        if point==-1:   #不存在小数点
            ret+=(new_s if len(new_s)==n else new_s+'0'*(n-len(new_s)))+"*10^"+str(len(s))
        else:   #小数
            if point<start:     #小数点在有效数字前面
                ret+=(new_s if len(new_s)==n else new_s+'0'*(n-len(new_s)))+"*10^"+str(point-start+1)
            else:   #小数点在有效数字后面
                ret+=(new_s if len(new_s)==n else new_s+'0'*(n-len(new_s)))+"*10^"+str(point-start)
    return ret

n,a,b=input().split()
n=int(n)
new_a,new_b=changeForm(a,n),changeForm(b,n)
if new_a==new_b:
    print("YES",new_a,end="")
else:
    print("NO",new_a,new_b,end="")
