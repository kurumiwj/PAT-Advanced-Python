s1=input()
a=int(s1)
b=a*2
s2=str(b)
l1=list(s1)
l1=sorted(l1)
l2=list(s2)
l2=sorted(l2)
if l1==l2:
    print("Yes")
else:
    print("No")
print(b)

exit(0)