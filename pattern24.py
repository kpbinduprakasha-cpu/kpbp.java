a=int(input())
count=1+a
for i in range(2,a):
    if (a%i)==0:
        count=i+count
print(count)
