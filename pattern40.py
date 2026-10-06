a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if (i%6)==0:
        print(i,end=" ")
        count+=1
if count==0:
    print("No Numbers Found")
