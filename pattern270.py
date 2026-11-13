result1 = 1
result2 = 1

for i in range(5, 8):
    j = 2
    while (j < 6):
        if i < j:
            result2 = result2 + 1
        else:
            result1 = result1 + 1
        j = j + 1

print(result2)
print(result1)
