from itertools import permutations
s1=input()
s2=input()
s3=input()
if len(s1)>len(s2):
    s1,s2=s2,s1
d1={}
if len(s1)<len(s2)<len(s3):
    d1[s3[0]]=1 
    d1[s3[1]]=0
    d1[s2[0]]=9
a=[i for i in range(10)]
s5=(set(s1)|set(s2)|set(s3))
s6=list(s5)
for i,j in d1.items():
    s6.remove(i)
    a.remove(j)
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
        print(v1,v2,v3)
        return True
    return False
b=list(permutations(a,len(s6)))
for i in b:
    d={}
    d.update(d1)
    for j,k in zip(s6,i):
        d[j]=str(k)
    if ans(d):
        print(d)
        break
