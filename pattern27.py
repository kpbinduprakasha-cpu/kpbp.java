a=input()

string=len(a)
total=0
for i in a:
    total=total+(int(i)**string)
    
if total==int(a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
