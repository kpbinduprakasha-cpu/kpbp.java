t=int(input())
m=int(input())
n=int(input())
count=0
for i in range(m,n+1):
    if (i%t)==0:
        count=count+i
print(count)
