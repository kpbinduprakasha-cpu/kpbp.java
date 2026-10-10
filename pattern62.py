a=int(input())
b=int(input())
total=0
for i in range(1,b+1):
    power=2*i-1
    value=a**power
    
    if i%2==1:
        total=total+value
    else:
        total=total-value
print(total)
