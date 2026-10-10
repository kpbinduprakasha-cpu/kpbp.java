a=int(input())
for i in range(1,a+1):
    space=a-i
    gap=" "*space
    values=(str(i)+" ")*i
    print(gap+values)
for i in range(a-1,0,-1):
    space=a-i
    gap=" "*space
    values=(str(i)+" ")*i
    print(gap+values)
