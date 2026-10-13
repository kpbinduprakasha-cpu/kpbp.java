a=int(input())
for i in range(a,0,-1):
    if i==a:
        print("  "*(a-1)+"*")
    elif i==1:
        print("* "*a)
    else:
        space="  "*(i-1)
        midel="  "*(a-i-1)
        print(space+"* "+midel+"*")
