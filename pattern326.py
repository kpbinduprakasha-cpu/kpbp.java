a=int(input())
count=1
for i in range(a,0,-1):
    for j in range(1,i+1):
        if i==a or i==j or j==1:
            print(count,end=" ")
            count+=1
        else:
            print(" ",end=" ")
            count+=1
    print()
