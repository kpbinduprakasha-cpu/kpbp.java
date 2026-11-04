n = input()

even_digits_count = 0

for each_digit in n:
    each_digit = int(each_digit)
    if each_digit % 2 == 0:
        even_digits_count = even_digits_count + 1

if even_digits_count > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
