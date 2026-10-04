a=input()
b=int(input())
count=0
for i in range(1,b+1):
    value=(a*i)
    sum=int(value)
    count=count+sum
print(count)
