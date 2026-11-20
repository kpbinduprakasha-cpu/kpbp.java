n=int(input())
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i==n or j==1 or i==j):
            print(num,end=" ")
            num +=1
        else:
            print(" ",end=" ")
    print()
