a=int(input())
k=a*(a+1)//2
for i in range(a,0,-1):
    print("  "*(a-i),end="")
    for j in range(i):
        print(k,end=" ")
        k=k-1
    print()
