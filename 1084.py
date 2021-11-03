str_a=input()
str_b=input()
l=[]
for i in str_a:
    if i not in str_b:
        if i.upper() not in l:
            l.append(i.upper())
print(''.join(l))