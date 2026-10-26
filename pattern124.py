a=int(input())
for i in range(1,a+1):
    row=a-i
    space=row*" "
    print(space+i*"* ")
for i in range(a-1,0,-1):
    row=a-i
    space=row*" "
    if i==1:
        print(space+"*")
    else:
        inner_space=((2*i)-3)*" "
        print(space+"*"+inner_space+"*")