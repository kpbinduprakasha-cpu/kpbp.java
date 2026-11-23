n=int(input())
for i in range(1,n+1):
    if (i==1):
        row=""
        row +=(n-1)*(" ")+"5 "
        print(row)
    elif (i==n):
        row=""
        for j in range(n):
            print(5+j,end=" ")
        print()
    else:
        row=""
        left_space=n-i
        midile_space=2*i-4
        row+=left_space*" "+"5 "+midile_space*" "+str(i+4)+" "
        print(row)
