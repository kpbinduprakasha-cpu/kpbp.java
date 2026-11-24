m=int(input())
n=int(input())
count=m+n*(n+1)//2-1
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if i==n or j==i or j==1:
            print(count,end=" ")
        else:
            print(" ",end=" ")
        count-=1
    print()