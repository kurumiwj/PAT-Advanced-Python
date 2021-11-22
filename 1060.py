def isZero(s):
    n=len(s)
    for i in range(n):
        if s[i]!='0':
            return False
    return True

def removePrefixZeroes(s):
    start,index=0,0
    while index<len(s):
        if s[index]!='0':
            start=index
            break
        index+=1
    ret=s[start:]
    return ret

n,a,b=input().split()
n=int(n)
a,b=[a],[b]
if a[0].find('.')!=-1: #以小数点分割
    a=a[0].split('.')
if b[0].find('.')!=-1:
    b=b[0].split('.')
if n>=(len(a[0]+a[1]) if len(a)>1 else len(a[0])):  #如果有效位数超过a的整数部分加小数部分(如果有)
    new_a=a[0]+a[1] if len(a)>1 else a[0]
    new_a+='0'*(n-len(new_a))
else:   #有效位数不超过a的总长度
    new_a=a[0][:n] if n<=len(a[0]) else a[0]+removePrefixZeroes(a[1])[:(n-len(a[0]))]   #有效位数比整数小直接截取整数部分即可,否则还得加上超过整数位数的小数部分
if n>=(len(b[0]+b[1]) if len(b)>1 else len(b[0])):  #如果有效位数超过b的整数部分加小数部分(如果有)
    new_b=b[0]+b[1] if len(b)>1 else b[0]
    new_b+='0'*(n-len(new_b))
else:   #有效位数不超过b的总长度
    new_b=b[0][:n] if n<=len(b[0]) else b[0]+removePrefixZeroes(b[1])[:(n-len(b[0]))]   #有效位数比整数小直接截取整数部分即可,否则还得加上超过整数位数的小数部分
if new_a[:n]!=new_b[:n] or len(a[0])!=len(b[0]):
    print("NO 0.{:s}*10^{:d} 0.{:s}*10^{:d}".format(new_a[:n],len(a[0]) if not isZero(new_a) else len(a[0])-1,new_b[:n],len(b[0]) if not isZero(new_b) else len(b[0])-1),end="")
else:
    print("YES 0.{:s}*10^{:d}".format(new_a[:n],len(a[0]) if not isZero(new_a) else len(a[0])-1),end="")
