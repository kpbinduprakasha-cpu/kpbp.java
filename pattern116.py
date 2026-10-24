a=int(input())
for i in range(1,a+1):
    if i==1:
        print(str(i)+" ")
    else:
        spacee="  "*(i-2)
        print(str(i)+" "+spacee+str(i)+" ")
for i in range(a-1,0,-1):
    if i==1:
        print(str(i)+" ")
    else:
        spacee="  "*(i-2)
        print(str(i)+" "+spacee+str(i)+" ")
