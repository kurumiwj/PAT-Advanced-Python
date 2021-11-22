n,head=map(int,input().split())
l=[]
l1=[]
index={}    #记录每个地址所在的下标
for i in range(n):
    l.append(tuple(map(int,input().split())))
    index[l[i][0]]=i
start=head
if start not in index:  #不在已存在的下标中
    print("0 -1")
else:
    while l[index[start]][2]!=-1:   #该步骤是去除掉不在链表里的元素
        l1.append(l[index[start]])
        start=l[index[start]][2]
    l1.append(l[index[start]])
    l1.sort(key=lambda x:x[1])
    print("{:d} {:05d}".format(len(l1),l1[0][0]))
    for i in range(len(l1)):
        if i!=len(l1)-1:
            print("{:05d} {:d} {:05d}".format(l1[i][0],l1[i][1],l1[i+1][0]))
        else:
            print("{:05d} {:d} -1".format(l1[i][0],l1[i][1]))
