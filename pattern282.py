a=int(input())
n=int(input())
for i in range(n):
    for s in range(n-i-1):
        print(" ",end="")
            
    for j in range(i+1):
        value=j+a
        print(value,end=" ")
    print()
