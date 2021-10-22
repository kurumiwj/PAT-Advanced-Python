digit=["zero","one","two","three","four","five","six","seven","eight","nine"]
n=input()
sum=0
for i in range(len(n)):
    sum+=int(n[i])
sum=str(sum)
for i in range(len(sum)):
    print(digit[int(sum[i])],end="")
    if i!=len(sum)-1:
        print(" ",end="")
exit(0)
# def add(str1,str2):
#     ret=""
#     carry=0
#     i=len(str1)-1;
#     j=len(str2)-1;
#     while i>=0 and j>=0:
#         tmp=int(str1[i])+int(str2[j])+carry
#         carry=int(tmp/10)
#         ret+=str(tmp%10)
#         i-=1
#         j-=1
#     while i>=0:
#         tmp=int(str1[i])+carry
#         carry=int(tmp/10)
#         ret+=str(tmp%10)
#         i-=1
#     while j>=0:
#         tmp=int(str2[j])+carry
#         carry=int(tmp/10)
#         ret+=str(tmp%10)
#         j-=1
#     ret=ret[::-1]
#     return ret

