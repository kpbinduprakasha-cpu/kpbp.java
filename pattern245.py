total = 0

for i in range(1, 5):
    for j in range(1, 5):
        if j == 3:
            break
        total = total + j

print(total)
