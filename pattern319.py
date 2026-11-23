a=int(input())
b=int(input())
for i in range(1,a+1):
    for j in range(1,2*a):
        
        if i==1 and j%2 !=0:
            print(b+(j-1)//2,end=" ")
        
        elif j==i:
            print(b,end=" ")
        
        elif j==2*a-i:
            print(b+a-i,end=" ")
        
        else:
            print("",end=" ")
    print()
