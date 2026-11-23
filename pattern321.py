a=int(input())
b=int(input())
for i in range(1,a+1):
    for j in range(1,b+1):
        num=(i-1)*b+j
        if i==a or j==b or j==1 or i==1:
            print(num,end=" ")
        else:
            print(" ",end=" ")
    print()
