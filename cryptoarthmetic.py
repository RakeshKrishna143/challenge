from itertools import permutations
s1='KANSAS'
s2='OHIO'
s3='OREGON'
s4='O'
v=5
a=[i for i in range(10)]
a.remove(v)
s5=(set(s1)|set(s2)|set(s3))-set(s4)
s6=list(s5)

def value(d,s1):
    v=''
    for i in s1:
        v+=str(d[i])
    return int(v)

def ans(d):
    v1=value(d,s1)
    v2=value(d,s2)
    v3=value(d,s3)
    if v1+v2==v3:
        return True
    return False


b=list(permutations(a,len(s6)))
for i in b:
    d={}
    d[s4]=v
    for j,k in zip(s6,i):
        d[j]=str(k)
    if ans(d):
        print(d)
        break
