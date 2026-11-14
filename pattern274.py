a=int(input())
b=int(input())
count=0
for i in range(1,a+1):
    value=""
    for i in range(1,b+1):
        count=count+1
        value=value+str(count)+" "
    print(value)
