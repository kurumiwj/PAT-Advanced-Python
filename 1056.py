n,m=map(int,input().split())
weight=list(map(int,input().split()))   #每只老鼠的重量
order=list(map(int,input().split()))    #按照order顺序分组
new_weight=[]
for i in range(n):
    new_weight.append(weight[order[i]])
win=order  #存放每轮获胜选手的下标
group=int(n/m)+1 if n%m!=0 else int(n/m)
trank=group+1  #每组老鼠的排名
rank=[trank]*n
index=0
while len(win)!=1:
    group=int(len(win)/m)+1 if len(win)%m!=0 else int(len(win)/m)   #这里取整要注意不满一组的情况
    trank=group+1
    for i in win:
        rank[i]=trank
    win=[]
    index=0
    for i in range(group):
        max_weight=max(new_weight[index:index+m])
        win_index=weight.index(max_weight)
        win.append(win_index)
        index+=m
    new_weight=[]
    for i in win:
        new_weight.append(weight[i])
rank[win[0]]=1
print(*rank)
