a=int(input())
for i in range(a,0,-1):
    if a==i:
        print("* "*i)
    elif i==1:
        print("* ")
    else:
        space="  "*(i-2)
        print("* "+space+"* ")
