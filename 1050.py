s1=list(input())
s2=set(input())
i=0
while(True):
    if s1[i] in s2:
        del s1[i]
    else:
        i+=1
    if i>=len(s1):
        break
print("".join(s1))