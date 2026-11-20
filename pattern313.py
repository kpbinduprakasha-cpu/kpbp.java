a=int(input())
for i in range(1,a+1):
    row=""
    space=(a-i)*" "
    
    for j in range(1,i+1):
        row=row+str(j)+" "
    print(space+row)
