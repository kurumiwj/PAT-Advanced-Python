n,k=map(int,input().split())
course={}
for i in range(n):
    tmp=input().split()
    for j in range(2,len(tmp)):
        if course.get(tmp[j])==None:    #未统计过这门课
            course[tmp[j]]=[tmp[0]]
        else:   #已经统计过这门课
            course[tmp[j]].append(tmp[0])
for i in range(1,k+1):
    if str(i) in course:
        print(i,len(course[str(i)]))
        course[str(i)].sort()
        for j in course[str(i)]:
            print(j)
    else:
        print(i,0)
