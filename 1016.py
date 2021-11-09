def calTimeBill(start,end):
    global rate
    l_start=list(map(int,start.split(':')[1:]))
    s=(l_start[0]-1)*24*60+l_start[1]*60+l_start[2]
    total=sum(rate)*60
    bs=(l_start[0]-1)*total
    for i in range(l_start[1]):
        bs+=60*rate[i]
    bs+=rate[l_start[1]]*l_start[2]
    l_end=list(map(int,end.split(':')[1:]))
    e=(l_end[0]-1)*24*60+l_end[1]*60+l_end[2]
    be=(l_end[0]-1)*total
    for i in range(l_end[1]):
        be+=60*rate[i]
    be+=rate[l_end[1]]*l_end[2]
    return (e-s,(be-bs)/100)

def cmp(s):
    name=s[0][0]
    l=list(map(int,s[1][0].split(':')))
    return (name,l[0],l[1],l[2],l[3])

def total(name,l):   #计算总时间和总金钱
    t_time=0  #每个时间段的时间
    t_bill=0.0  #每个时间段的费用
    month=int(l[0][0].split(':')[0])    #月份
    print("{:s} {:02d}".format(name,month))
    total_bill=0.0
    for i in range(0,len(l),2):
        print(l[i][0][3:],l[i+1][0][3:],end=" ")
        (t_time,t_bill)=calTimeBill(l[i][0],l[i+1][0])
        print("{:d} ${:.2f}".format(t_time,t_bill))
        total_bill+=t_bill
    print("Total amount: $%.2f" % total_bill)

rate=list(map(int,input().split()))
n=int(input())
l=[]
lasting={}
for i in range(n):
    l.append(list(zip(input().split())))
l.sort(key=lambda x:cmp(x))   #按照时间从小到大排序
for i in l:
    name=i[0][0]    #姓名
    status=i[2][0]  #on或off状态
    t=i[1][0]   #时间
    if lasting.get(name)==None: #若该姓名还未出现过
        if status=="off-line":
            continue
        else:
            lasting[name]=[(t,status)]
    else:   #该姓名已经出现
        if lasting[name][-1][1]!=status:    #此人上一次状态与这次不一样则收录
            lasting[name].append((t,status))
        else:
            if status=="on-line":   #若此人上一次状态与这次一样且是on则将上一次收录的结果覆盖
                lasting[name][-1]=(t,status)
            elif status=="off-line":    #若此人上一次状态与这次一样且是off则忽略此次记录
                continue
key=lasting.keys()
for i in key:
    if len(lasting[i])%2!=0:
        lasting[i].pop()
    if len(lasting[i])!=0:
        total(i,lasting[i])

