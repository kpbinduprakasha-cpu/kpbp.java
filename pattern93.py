a=int(input())
for i in range(a+1,0,-1):
    v=a+1
    if i==a+1:
        print("_"*v)
    else:
        space=" "*(i-1)
        print("|"+space+"/")
