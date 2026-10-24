a=int(input())
for i in range(1,a+1):
    left_space=" "*(a-i)
    if i ==1:
        print(left_space+"*")
    else:
        hollow_spaces=" "*(2*i-3)
        print(left_space+"*"+hollow_spaces+"*")
for i in range(a-1,0,-1):
    left_space=" "*(a-i)
    if i ==1:
        print(left_space+"*")
    else:
        hollow_spaces=" "*(2*i-3)
        print(left_space+"*"+hollow_spaces+"*")
