a = int(input())
count = 0
while a > 0:
    digit = a % 10
    if digit % 2 == 0:
        count = count + 1
    a = a // 10
if count > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
