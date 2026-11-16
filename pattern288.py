a=int(input())
b=int(input())
c=a*b
value=c
for i in range(1,a+1):
    for j in range(1,b+1):
        print(value,end=" ")
        value=value-1
    print()
