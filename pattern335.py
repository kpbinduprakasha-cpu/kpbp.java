a=int(input())
for i in range(1,2*a):
    if i==1 or i==a or i==2*a-1:
        print("* "*a)
    elif i<a:
        print("  "*(a-1)+"* ")
    else:
        print("* ")