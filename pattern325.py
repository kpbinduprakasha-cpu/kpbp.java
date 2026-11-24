a=int(input())
b=int(input())
for i in range(1,b+1):
    for j in range(1,b+1):
        if j<i:
            print(" ",end=" ")
        elif i==1 or i==j or j==b:
            print(a,end=" ")
            a+=1
        else:
            print(" ",end=" ")
    print()
