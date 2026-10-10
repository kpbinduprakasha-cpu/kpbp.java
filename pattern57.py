a=int(input())
for i in range(1,a+1):
    space=a-i
    gap=" "*(2*space)
    plus="+ "*(i-1)
    print(gap+plus+"#")
for i in range(a-1,0,-1):
    space=a-i
    gap=" "*(2*space)
    plus="+ "*(i-1)
    print(gap+plus+"#")
