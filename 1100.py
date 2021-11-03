low=["tret","jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]  #低位
high=["tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"] #高位

def earth_to_mars(n):
    ret=""
    h=int(n/13)-1
    l=n%13
    if h>=0:
        ret+=high[h]
        if l!=0:
            ret+=" "+low[l]
    else:
        ret+=low[l]
    return ret

def mars_to_earth(l):
    num=0
    if len(l)==1:
        s=l[0]
        if s in low:
            num+=low.index(s)
        else:
            num+=(high.index(s)+1)*13
    else:
        s1,s2=l[0],l[1]
        num+=(high.index(s1)+1)*13+low.index(s2)
    return num

n=int(input())
for i in range(n):
    s1=input()
    if s1.isdigit():
        print(earth_to_mars(int(s1)))
    else:
        l=s1.split()
        print(mars_to_earth(l))