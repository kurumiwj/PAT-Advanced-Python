capacity,distance,d,n=map(int,input().split())
longest=capacity*d
station=[]
for i in range(n):
    tmp=input().split()
    price,dis=float(tmp[0]),int(tmp[1])
    station.append(tuple([price,dis]))
station.sort(key=lambda x:(x[1],x[0])) #按距离从小到大排序
index=0
dis=0
total_price=0  #统计总油价
total_gas=0  #统计车内还剩的油量能开的距离
next_index=0  #记录下一个停靠的加油站的下标
cannt_reach=False  #记录是否已经判断过不能到达
if station[0][1]==0:    #位置0处必须有一个加油站否则直接跳出
    if longest>distance:    #如果汽车一次能跑的最远距离已经超过目的地和出发地之间的距离
        total_price+=station[0][0]*distance/d
        print("%.2f"%total_price)
    else:
        while index<n:   #在起点终点之间遍历最少价格
            p,start=station[next_index][0],station[next_index][1] #记录起点处的油价和位置
            total_gas-=dis
            index=next_index+1
            flag=False  #记录汽车行程内是否有加油站
            if index==n:
                break
            next_p,next_dis=station[index][0],station[index][1]
            next_index=index
            while station[index][1]<=start+longest: #若超出汽车加满油能跑到的最远距离
                flag=True
                if station[index][0]<=p: #若加油站费用小于或等于当前费用则开到那个加油站
                    next_index=index
                    break
                else:   #否则在当前加油站加满油之后开到下一个最低价格的加油站
                    if station[index][0]<next_p:
                        next_p,next_dis,next_index=station[index][0],station[index][1],index
                    index+=1
            if flag:
                dis=station[next_index][1]-start
                if station[next_index][0]>p:    #若下一个加油站油价比当前的要贵则全部加满油
                    total_price+=p*(longest-total_gas)
                    total_gas=longest
                else:   #下一站油价比当前便宜则加够到下一个加油站的油量
                    if dis>total_gas:  #如果余下的油量不够跑到下一个目标加油站则加油
                        total_price+=(dis-total_gas)*p
                        total_gas=dis
                    else:   #如果余下的油量够跑到下一个目标加油站则不加油
                        continue
            else:
                cannt_reach=True
                print("The maximum travel distance = %.2f"%(start+longest))
                break
        if not cannt_reach:
            if start+longest<distance:  #无法到达
                print("The maximum travel distance = %.2f"%(start+longest))
            else:
                total_price+=(distance-start)*p
                print("%.2f"%(total_price/d))
else:
    print("The maximum travel distance = 0.00")
