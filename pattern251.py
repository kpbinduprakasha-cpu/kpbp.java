total = 0

for i in range(1, 5):
    for j in range(1, 5):
        total = total + j
        if total >= 15:
            break
    if total >= 15:
        break

print(total)
