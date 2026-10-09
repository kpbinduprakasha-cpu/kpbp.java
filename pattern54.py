a=int(input())
count=0
for i in range(1,a+1):
    space=a-i
    star="* "*i
    gap="  "*(2*space)
    print(star+gap+star)
