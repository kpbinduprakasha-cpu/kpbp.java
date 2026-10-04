a=input()
b=int(input())
count=0
for i in range(1,b+1):
    valus=int(i*a)
    valus=valus**2
    count=count+valus
print(count)
