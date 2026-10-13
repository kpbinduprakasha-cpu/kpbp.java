a=int(input())
for i in range(1,a+1):
    if i==a:
        print("* "*a)
    elif i==1:
        print("*")
    else:
        space="  "*(i-2)
        print("* "+space+"* ")
