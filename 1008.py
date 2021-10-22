up=6 #上楼时间
down=4 #下楼时间
stay=5 #每层楼停留时间
l=input().split()
n=int(l[0])
floor=list(map(int,l[1:]))
start=0 #起始楼层
total_time=0 #总时间
for i in range(n):
    if floor[i]>start: #上楼
        total_time+=(floor[i]-start)*6+5
    elif floor[i]<start: #下楼
        total_time+=(start-floor[i])*4+5
    else:
        total_time+=5
    start=floor[i]
print(total_time)
exit(0)