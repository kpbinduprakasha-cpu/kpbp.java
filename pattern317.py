n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        if i==j or i==n or j==1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
