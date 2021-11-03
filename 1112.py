k=int(input())
s=input()
index=0
isStucked={}
ret=""
stucked=[]
while index<len(s):
    for i in range(1,k):
        if index+i>=len(s):
            isStucked[s[index]]=False
            index+=i
            break
        if s[index+i]!=s[index]:
            isStucked[s[index]]=False
            index+=i
            break
        elif i==k-1:
            isStucked[s[index]]=True
            index+=k
i=0
while i<len(s):
    if isStucked[s[i]]==False:
        ret+=s[i]
        i+=1
    else:
        if s[i] not in stucked:
            stucked.append(s[i])
        ret+=s[i]
        i+=k
print(''.join(stucked))
print(ret)
