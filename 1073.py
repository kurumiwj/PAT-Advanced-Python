import math

l=input().split('E')
n=int(l[1])
t=list(l[0])
s=""
if t[0]=='+':   #去掉开头的+号
    t.pop(0)
dot=t.index('.')    #找到小数点位置
fracLen=len(t[dot+1:])  #小数部分总位数
if n<0: #指数小于0
    if t[0]=='-':   #底数是负数
        s+=t[0]+'0.'+'0'*(abs(n)-1)
        t.remove('.')
        s+=''.join(t[1:])
    else:
        s+='0.'+'0'*(abs(n)-1)
        t.remove('.')
        s+=''.join(t[:])
elif n==0:  #指数等于0
    s=t
else:   #指数大于0
    if fracLen<=n:  #小数部分长度小于指数
        t.remove('.')
        t.extend(list('0'*(n-fracLen)))
        s=t
    else:   #小数部分长度大于指数
        s+=''.join(t[0:dot])+''.join(t[dot+1:dot+n+1])+'.'+''.join(t[-(fracLen-n):])
print(''.join(s))