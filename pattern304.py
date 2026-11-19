m=int(input())
n=int(input())
for i in range(m,n+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count +=1
    if count>0:
        print(i)
