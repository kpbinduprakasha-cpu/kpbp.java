a=int(input())
count=a
for i in range(a):
    value=count-i
    row=(str(value)+" ")*value
    print(row)
