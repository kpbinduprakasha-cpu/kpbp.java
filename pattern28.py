a=int(input())
b=int(input())
greatest_number=b
for i in range(a-1):
    number=int(input())
    if number>greatest_number:
        greatest_number=number
print(greatest_number)
