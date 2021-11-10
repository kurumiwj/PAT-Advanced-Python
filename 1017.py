def cmp(l): #日期格式HH:MM:SS
    l=list(map(int,l.split(':')))
    return (l[0],l[1],l[2])

def timeChange(t):  #统一时间成秒来处理
    t=list(map(int,t.split(':')))
    tm=t[0]*3600+t[1]*60+t[2]
    return tm

n,k=map(int,input().split())
customer=[]
for i in range(n):
    t=tuple(input().split())
    customer.append(t)
customer.sort(key=lambda x:cmp(x[0]))
end=[]
wait_time=0
for i in customer:
    t=list(map(int,i[0].split(':')))
    start=timeChange(i[0])
    if t[0]>17 or t[0]==17 and (t[1]>0 or t[2]>0):  #去掉17点以后来的人
        customer.remove(i)
        n-=1
        continue
    elif t[0]<8:    #如果来的时间早于8点则置为8点
        wait_time+=timeChange("08:00:00")-start #来的早的人一样要等
        start=timeChange("08:00:00")    #初始时间置为8点
    if len(end)==k:  #窗口已满需要处理，否则什么都不做
        if start>=end[-1]:  #每来一个人就处理正在办理的人，看是否有走掉的人(不止处理一个，而是把前面所有办理好的人全部清掉)
            while start>=end[-1]:
                end.pop()
                if len(end)==0:
                    break
        else:   #如果来的时间早于最早结束那个人的时间则需要等待
            wait_time+=end[-1]-start
            start=end[-1]
            end.pop()
    end.append(start+int(i[1])*60)
    end.sort(reverse=True)
print("%.1f" % (wait_time/n/60))
