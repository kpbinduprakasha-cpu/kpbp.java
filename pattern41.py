a=int(input())
b=int(input())
sum=0
for i in range(1,b+1):
    value=a**(2*i)
    if i %2==0:
        value=-value
    sum=sum+value 
print(sum)
