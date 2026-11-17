a=int(input())
b=int(input())
k=a
for i in range(1,b+1):
    for j in range(i):
        print(k,end=" ")
        k=k+1
    print()
