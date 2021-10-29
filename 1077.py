n=int(input())
l=[]

def isInList(s):
    for i in l:
        if s not in i:
            return False
    return True

for i in range(n):
    l.append(input())
l.sort(key=lambda x:len(x))
length=0
s=l[0]
index=len(s)
if isInList(s[index-1]):
    length=1
    for i in range(index-1,-1,-1):
        if isInList(s[i:]):
            length+=1
        else:
            break
if length!=0:
    print(s[index-length+1:])
else:
    print("nai")