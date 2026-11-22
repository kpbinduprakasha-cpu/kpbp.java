n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
