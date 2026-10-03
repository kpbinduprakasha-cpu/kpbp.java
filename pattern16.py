m = int(input())
n = int(input())

total_numbers = n - m
odd_numbers = ""

for i in range(total_numbers + 1):
    number = n - i
    is_odd = (number % 2 != 0)
    if is_odd:
        odd_numbers = odd_numbers + str(number) + (" ")

print(odd_numbers)
