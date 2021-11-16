def isSymmetric(s):
    start,end=0,len(s)-1
    while start<=end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

s=input()
start=0
maxL=1
while start<len(s)-1:
    end=start+1
    while end<len(s):
        length=end-start+1
        if length<maxL:
            end+=1
            continue
        if s[end]==s[start] and isSymmetric(s[start:end+1]):
            maxL=max(length,maxL)
        end+=1
    start+=1
print(maxL)
