def gcd(a,b):
    return  0 if a==0 else a if b==0 else gcd(b,a%b)

def simplify(a,b):
    g=gcd(a,b)
    if g==0:
        return 0,b
    else:
        a=int(a/g)
        b=int(b/g)
        return a,b

def formatter(a,b): #格式化输出
    if a==0:    #分子为0必然是0
        return "0"
    ret=""
    if abs(a)<b:    #a的绝对值小于b
        if a>0:
            ret+=str(a)
            if b!=1:    #分母不为1时再输出
                ret+='/'+str(b)
        else:
            ret+='('+str(a) #负数要加括号
            if b!=1:
                ret+='/'+str(b)
            ret+=')'
    else:
        k=int(abs(a)/b) #整数部分
        if a<0:
            ret+='(-'
        ret+=str(k)
        t=abs(a)%b
        if t!=0:
            ret+=' '+str(t)+'/'+str(b)
        if a<0:
            ret+=')'
    return ret

def operator(a1,b1,a2,b2,op):
    num1=formatter(a1,b1)
    num2=formatter(a2,b2)
    print(num1+' '+op+' '+num2+' = ',end="")
    g=gcd(b1,b2)
    denominator=(int)(b1/g*b2)
    numerator1=(int)(a1*b2/g)
    numerator2=(int)(a2*b1/g)
    if op=='+':
        numerator=numerator1+numerator2
        a,b=simplify(numerator,denominator)
        print(formatter(a,b))
    elif op=='-':
        numerator=numerator1-numerator2
        a,b=simplify(numerator,denominator)
        print(formatter(a,b))
    elif op=='*':
        denominator=b1*b2
        numerator=a1*a2
        a,b=simplify(numerator,denominator)
        print(formatter(a,b))
    else:
        if num2=='0':
            print("Inf")
        else:
            denominator=b1*a2
            numerator=b2*a1
            a,b=simplify(numerator,denominator)
            print(formatter(a,b))

l=input().split()
a1,b1=map(int,l[0].split('/'))
a2,b2=map(int,l[1].split('/'))
a1,b1=simplify(a1,b1)
a2,b2=simplify(a2,b2)
operator(a1,b1,a2,b2,'+')
operator(a1,b1,a2,b2,'-')
operator(a1,b1,a2,b2,'*')
operator(a1,b1,a2,b2,'/')
