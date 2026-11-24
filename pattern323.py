a=int(input())
b=int(input())
for i in range(1,b+1):
    for j in range(1,b+1):
        if i==b or i==1 or j==b or j==1:
            print(a,end=" ")
            a+=1
        else:
            print(" ",end=" ")
            a+=1
    print()
