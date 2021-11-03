def isLegal(s):
    index=s.find('.')
    if index==-1: #不含小数点
        if not s.isdigit():
            return False
        else:
            sn=float(s)
            if sn>1000 or sn<-1000: #不在要求范围内
                return False
    else:
        s1,s2=s[:index] if s[0]!='-' else s[1:index],s[index+1:]    #分成整数和小数两部分
        if (s1!="" and not s1.isdigit()) or (s2!="" and not s2.isdigit()) or len(s2)>2:
            return False
        elif abs(int(s1))>1000 or abs(int(s1))==1000 and int(s2)>0: #单独考虑整数部分为1000的情况，不然测试点3报错
            return False
    return True

n=int(input())
l=input().split()
sum=0.0
cnt=0
for i in l:
    if not isLegal(i):
        print("ERROR: %s is not a legal number" % i)
    else:
        sum+=float(i)
        cnt+=1
if cnt==1:
    print("The average of 1 number is %.2f" % sum)
elif cnt==0:
    print("The average of 0 numbers is Undefined")
else:
    print("The average of {:d} numbers is {:.2f}".format(cnt,sum/cnt))