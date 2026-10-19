a=int(input())
for i in range(1,a+1):
    if i==1:
        space=(a-1)
        row=" "*space+"* "
    elif i==a:
        row="* "*a
    else:
        left=(a-i)
        hollow=2*(i-2)
        row=" "* left+"* "+" "*hollow+"* "
    print(row)
