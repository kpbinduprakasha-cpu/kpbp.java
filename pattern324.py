a=int(input())
b=int(input())
for i in range(1,b+1):
    for j in range(1,i+1):
        if i==b or i==j or j==1:
            print(a,end=" ")
            a+=1
        else:
            print(" ",end=" ")
    print()
