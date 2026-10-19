a=int(input())
print("# "*a)
for i in range(a-2,0,-1):
     space=(2*i)-1
     print("+"+" "*space+"+")
if a>1:
    print("+")
