a=int(input())
for i in range(1,2*a):
    if i==1 or i==a or i==2*a-1:
        each_rows="* "*(a)
    elif i<a:
        each_rows="* "
    else:
        spaces=" "*(2*(a-2))
        each_rows="* "+spaces+"* "
    print(each_rows)