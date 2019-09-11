day={0:'sun',1:'mon',2:'tue',3:'wed',4:'thurs',5:'fri',6:'sat'}
month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
odd=0
def isleap(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
string='15 aug 2010'
string=string.split()
n1=int(string[2])-1
n=n1
a=[2000,1600,1200,800,400]
for i in a:
    n=n%i 
n,odd=(n%100,(n//100)*5)
for i in range(n1-n+1,n1+1):
    if isleap(i):
        odd+=2 
    else:
        odd+=1 
for i,j in zip(month,month_days):
    if string[1]==i:
        break
    if isleap(int(string[2])) and string[1]=='feb':
        odd+=1
    odd+=j
odd+=int(string[0])
odd=odd%7 
print(day[odd])
