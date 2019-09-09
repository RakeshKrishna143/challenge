n=7

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=(n//2)+1+1 and i+j<=(n//2)+1+n and i-j<=(n//2) and j-i<=(n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
