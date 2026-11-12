total = 0
iterations = 0

for i in range(1, 10, 3):
    for j in range(2, 8, 2):
        total = total + (i + j)
        iterations = iterations + 1

print("Iterations:", iterations)
print("Total:", total)
