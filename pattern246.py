total = 0

for i in range(1, 4):
    for j in range(1, 5):
        if j % 2 == 0:
            continue
        total = total + (i + j)

print(total)
