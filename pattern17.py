m=int(input())
n=int(input())
count=1
for i in range(m,n+1):
    if (i%3==0):
        count=count*i
print(count)
