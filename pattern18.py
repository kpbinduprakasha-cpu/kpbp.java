n=int(input())
m=int(input())
count=0
value=0
for i in range(1,n+1):
    value=i**m
    count=count+value
print(count)
