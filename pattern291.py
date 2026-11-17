a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,i):
        print(j,end=" ")
    print()
