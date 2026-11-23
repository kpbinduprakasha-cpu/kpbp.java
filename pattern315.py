n=int(input())
for i in range(1,n+1):
    if i==1:
        row=""
        row=row+(n-1)*(" ")+"1 "
        print(row)
    elif (i==n):
        row=""
        for j in range(n):
            print(1+j,end=" ")
        print()
    else:
        row=""
        left_space=n-i
        midile_space=2*i-4
        row=row+left_space*" "+"1 "+midile_space*" "+str(i)+" "
        print(row)
