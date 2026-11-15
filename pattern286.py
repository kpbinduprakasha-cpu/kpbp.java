a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
            count +=1
if count==0:
    print("No Prime Numbers Found")
