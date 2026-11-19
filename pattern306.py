number = 7
total = 0

for i in range(1, number + 1):
    if ((i % 2) == 0):
        continue
    total = total + i

print(total)
