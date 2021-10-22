a,b=map(int,input().split())
sum=a+b
absSum=abs(sum)
if absSum<1000:
    print(sum)
elif absSum<1000000:
    if sum>0:
        print("%d,%03d" % (absSum/1000,absSum%1000))
    else:
        print("-%d,%03d" % (absSum/1000,absSum%1000))
else:
    if sum>0:
        print("%d,%03d,%03d" % (absSum/1000000,absSum%1000000/1000,absSum%1000))
    else:
        print("-%d,%03d,%03d" % (absSum/1000000,absSum%1000000/1000,absSum%1000))

exit(0)