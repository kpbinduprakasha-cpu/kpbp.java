a=int(input())
for i in range(a,0,-1):
    if i==a:
        print("* "*a)
    else:
        leading=(a-i)*"  "
        if i>1:
            inner=(i-2)*"  "
            print(leading+"* "+inner+"* ")
        else:
            print(leading+"* ")
