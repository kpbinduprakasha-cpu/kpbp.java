a=int(input())
capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,a+1):
    for j in range(a):
        print(capital[j],end=" ")
    print()