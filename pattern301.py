n=int(input())
k=int(input())
count=0
for i in range(1,k+1):
    count=count+i

num=n+count-1

for i in range(1,k+1):
    for j in range(i):
        print(num,end=" ")
        num=num-1
    print()
