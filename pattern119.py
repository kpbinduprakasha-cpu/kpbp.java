a=int(input())
for i in range(1,a+1):
    space="  "*(a-i)
    if i==1:
        print(space+str(i)+" ")
        
    else:
        mid_space="  "*(i-2)
        print(space+str(i)+" "+mid_space+str(i)+" ")
 
for i in range(a-1,0,-1):
    space="  "*(a-i)
    if i==1:
        print(space+str(i)+" ")
        
    else:
        mid_space="  "*(i-2)
        print(space+str(i)+" "+mid_space+str(i)+" ")
