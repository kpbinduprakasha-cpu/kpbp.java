a=int(input())

for i in range(1,a+1):
    value=a+1
    sorce=value-i
    if (a==sorce):
        print("* "*sorce)
    else:
        print("+ "*sorce)
