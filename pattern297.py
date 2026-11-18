a=int(input())
b=int(input())
c=a+(b*(b+1))//2-1
for i in range(b,0,-1):
    for j in range(1,i+1):
        print(c,end=" ")
        c -=1
    print()
