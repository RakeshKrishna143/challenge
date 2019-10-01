n=5
a=[[0 for j in range((2*n)-1)]for i in range(n)]
for i in range(n):
    for j in range((2*n)-1):
        if i+j==n-1 or j-i==n-1:
            a[i][j]=1 
for i in range(1,n):
    for j in range(1,(2*n)-2):
        a[i][j]=a[i-1][j-1]+a[i-1][j+1]
   
            
for i in range(n):
    for j in range((2*n)-1):
        if a[i][j]!=0:
            print(a[i][j],end='')
        else:
            print(' ',end='')
    print()
