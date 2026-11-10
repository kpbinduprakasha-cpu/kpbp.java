num = input()
power = len(num)
total = 0
for digit in num:
    total = total + int(digit) ** power
if total == int(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
