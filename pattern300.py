a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    s=0
    power=len(str(i))
    
    while temp>0:
        digite=temp%10
        s=s+digite**power
        temp=temp//10
        
    if s==i:
        print(i,end=" ")
