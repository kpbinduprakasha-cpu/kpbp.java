n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        row=("* ")*n
    else:
        spaces=2*n-4
        row="* "+" "*(2*n-4)+"* "
    print(row)
