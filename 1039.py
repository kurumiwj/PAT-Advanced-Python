n,k=map(int,input().split())
select_courses={}
for i in range(k):
    course,num=map(int,input().split())
    name=input().split()
    for j in name:
        if j not in select_courses:
            select_courses[j]=[course]
        else:
            select_courses[j].append(course)
query=input().split()
for i in range(len(query)):
    if query[i] in select_courses:
        total=len(select_courses[query[i]])
        select_courses[query[i]].sort()
    else:
        total=0
    print(query[i],total,end="")
    if total!=0:
        for j in select_courses[query[i]]:
            print(" "+str(j),end="")
    if i!=len(query)-1:
        print()
