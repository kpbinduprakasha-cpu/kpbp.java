even_count = 0
odd_count = 0

for i in range(1, 4):
    for j in range(1, 4):
        if (i + j) % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

print("Even pairs:", even_count)
print("Odd pairs:", odd_count)
