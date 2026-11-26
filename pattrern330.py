a=int(input())
total=0
for i in range(a):
    b=int(input())
    count=0
    for j in range(1,b+1):
        if b%j==0:
            count+=1
    if b>1 and count==2:
        total+=b
print(total)