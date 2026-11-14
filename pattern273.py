a=int(input())

count=0
for i in range(1,a+1):
    value=""
    for j in range(1,i+1):
        count=count+1
        value=value+str(count)+" "
    print(value)
