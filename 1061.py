week=["MON","TUE","WED","THU","FRI","SAT","SUN"]
s=[]
result=[]
for i in range(4):
    s.append(input())
n=min(len(s[0]),len(s[1]))
cnt=0
for i in range(n):
    if cnt==0:
        if s[0][i]==s[1][i] and s[0][i].isupper() and (ord(s[0][i])>=ord('A') and ord(s[0][i])<=ord('G')):
            cnt+=1
            result.append(week[ord(s[0][i])-ord('A')])
    elif cnt==1:
        if s[0][i]==s[1][i] and ((ord(s[0][i])>=ord('A') and ord(s[0][i])<=ord('N')) or s[0][i].isdigit()):
            if s[0][i].isdigit():
                result.append(int(s[0][i]))
            else:
                result.append(int(ord(s[0][i])-ord('A')+10))
            break
n=min(len(s[2]),len(s[3]))
for i in range(n):
    if s[2][i]==s[3][i] and s[2][i].isalpha():
        result.append(i)
print("{:s} {:02d}:{:02d}".format(result[0],result[1],result[2]))

exit(0)