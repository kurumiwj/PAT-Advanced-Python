n=int(input())
for i in range(n):
    num=list(input())
    num1=num[:int(len(num)/2)]
    num2=num[int(len(num)/2):]
    num=int(''.join(num))
    num1=int(''.join(num1))
    num2=int(''.join(num2))
    if num1==0 or num2==0 or num%(num1*num2)!=0:
        print("No")
    else:
        print("Yes")
