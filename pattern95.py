a=int(input())
b=int(input())
for i in range(1,a+1):
    if i==1 or i==a:
        print("* "*b)
    else:
        space="  "*(b-2)
        print("* "+space+"* ")
