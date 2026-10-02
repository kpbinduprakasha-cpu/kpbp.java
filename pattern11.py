a=int(input())
b=int(input())
count=0
for i in range(1,a+1):
    if (i%b)==0:
        count=count+1
print(count)
