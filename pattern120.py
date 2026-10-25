a=int(input())
b=(a*2)-2
space="  "*b
print("* "+space+"*")
h=-1
for i in range(2,a):
    h=h+1
    space="  "*h
    mp=(a*2)-(i+i)
    mspase="  "*mp
    print("* "+space+"* "+mspase+"* "+space+"*")
if 2*a>2:
    print("* "*2*a)
