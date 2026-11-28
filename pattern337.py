a=int(input())
b=(2*a)+2
for i in range(1,b):
    if i==1 or i==(b-1) or i==(a+1):
        print("* "*a)
    else:
        spaces=" "*(2*(a-2))
        value="* "+spaces+"* "
        print(value)