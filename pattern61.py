a=int(input())
count=0
for i in range(1,a+1):
    string=str(i)
    index=string[0:]
    lenth=len(index)
    count=count+lenth
print(count)
