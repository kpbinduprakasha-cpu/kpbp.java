a=int(input())

for i in range(a,0,-1):
    value=""
    for j in range(1,i+1):
        
        value=value+str(j)+" "
    print(value)
