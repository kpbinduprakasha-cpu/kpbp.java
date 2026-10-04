a=int(input())
count=""
for i in range(1,a+1):
    value=(a%i==0)
    if value:
        count=count+str(i)+" "
print(count)
