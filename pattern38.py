a=int(input())
divisabule=False
for i in range(2,10):
    if a%i==0:
        divisabule=True
   
if divisabule:
    print("Divisible Number")
else:
    print("Indivisible Number")
