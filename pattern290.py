a=int(input())
count=0
for i in range(1,a):
    for j in range(i+1,a):
        k=a-i-j
        if j<k:
            count=count+1
print(count)
