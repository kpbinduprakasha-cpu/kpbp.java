a=int(input())
for i in range(a):
    space=i
    value=a-i
    
    if a==value: 
        print(" "*space+"+ "*value)
    else:
        print(" "*space+"* "*value)
