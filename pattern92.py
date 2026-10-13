a=int(input())
for i in range(1,a+1):
    if i==1:
        print("* ")
    elif i==a:
        print("* "*a)
    else:
        space="  "*(i-2)
        print("* "+space+"* ")
