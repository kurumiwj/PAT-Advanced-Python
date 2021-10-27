color=list(map(int,input().split()))
st=""
l=["A","B","C"]
for i in range(len(color)):
    decade=(int)(color[i]/13)
    unit=color[i]%13
    if decade<10:
        st+=str(decade)
    else:
        st+=l[decade-10]
    if unit<10:
        st+=str(unit)
    else:
        st+=l[unit-10]
print("#"+st)