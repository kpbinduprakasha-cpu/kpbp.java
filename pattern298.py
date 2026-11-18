a=int(input())
count=0
for i in range(1,a+1):
    for j in range(2,11):
        if i%j ==0:
            break
    else:
            count=count+1
print(count)
