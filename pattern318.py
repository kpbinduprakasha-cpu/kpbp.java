n=int(input())
m=int(input())
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==n or j==m or i==1 or j==1:
            print(6+j,end=" ")
        else:
            print(" ",end=" ")
    print()
