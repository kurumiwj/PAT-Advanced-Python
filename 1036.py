n=int(input())
male=[]
female=[]
absent=False
for i in range(n):
    tmp=input().split()
    name=tmp[0]
    gender=tmp[1]
    id=tmp[2]
    grade=int(tmp[-1])
    member=tuple([name,id,grade])
    if gender=='M':
        male.append(member)
    else:
        female.append(member)
if len(female)!=0:
    female.sort(key=lambda x:-x[-1])
    print(female[0][0],female[0][1])
else:
    absent=True
    print("Absent")
if len(male)!=0:
    male.sort(key=lambda x:x[-1])
    print(male[0][0],male[0][1])
else:
    absent=True
    print("Absent")
if absent:
    print("NA")
else:
    print(abs(male[0][-1]-female[0][-1]))
