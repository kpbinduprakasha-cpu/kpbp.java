a=int(input())
for i in range(1,a+1):
    if i==1 or i==a:
        print("* "*a)
    else:
        space="0 "*(a-2)
        print("* "+space+"* ")
