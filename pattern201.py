a = input()
count = 0
for i in a:
    if i == "0":
        count = count + 1
if count > 3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")
