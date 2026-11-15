n=int(input())
 
for i in range(1,n+1):
    sum_of_power_digits=0
    i=str(i)
    power=len(i)
    
    for eanch_digit in i:
        eanch_digit=int(eanch_digit)
        sum_of_power_digits=sum_of_power_digits+(eanch_digit**power)
        
    i=int(i)
    is_armstrong=sum_of_power_digits==i
    
    if is_armstrong:
        print(i)
