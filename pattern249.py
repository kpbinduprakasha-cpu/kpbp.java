count = 0

for i in range(1, 5):
    for j in range(1, 5):
        if (i * j) % 3 == 0:
            count = count + 1

print(count)
