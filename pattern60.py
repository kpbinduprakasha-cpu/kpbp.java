a=int(input())
for i in range(a,0,-1):
    space=a-i
    gap=" "*space
    star="* "*i
    print(gap+star)
