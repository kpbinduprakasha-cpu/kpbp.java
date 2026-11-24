a=int(input())
b=int(input())
c=a*b
for i in range(1,a+1):
    for j in range(1,b+1):
        if i==a or i==1 or j==b or j==1:
            print(c,end=" ")
            c-=1
        else:
            print(" ",end=" ")
            c-=1
    print()
