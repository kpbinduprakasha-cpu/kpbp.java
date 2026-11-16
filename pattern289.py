n=int(input())
count=0
for i in range(1,n):
    b=n-i
    if i<b:
        count=count+1
print(count)
