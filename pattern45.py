a=int(input())
for i in range(a):
    space="  "*i
    values=a-i
    value=str(values)+" "
    print(space+value*values)
