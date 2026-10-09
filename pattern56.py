a=int(input())
for i in range(1,a+1):
    space=a-i
    star="* "*i
    gap="  "*(2*space)
    print(star+gap+star)
for i in range(a-1,0,-1):
    space=a-i
    star="* "*i
    gap="  "*(2*space)
    print(star+gap+star)
