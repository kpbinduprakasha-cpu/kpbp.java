max_val = 0

for i in range(1, 6):
    for j in range(i + 1, 6):
        val = i * j - (i + j)
        if val > max_val:
            max_val = val

print(max_val)
