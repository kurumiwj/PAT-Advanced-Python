def isPalindromic(s,start,end):
    while start<=end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

n=input()
cnt=0
flag=True
while not isPalindromic(n,0,len(n)-1):
    cnt+=1
    n=list(n)
    n_reverse=reversed(n)
    num1=int(''.join(n))
    num2=int(''.join(n_reverse))
    n=str(num1+num2)
    print(num1,'+',num2,'=',n)
    if cnt==10:
        flag=False
        print("Not found in 10 iterations.")
        break
if flag:
    print(n,"is a palindromic number.")