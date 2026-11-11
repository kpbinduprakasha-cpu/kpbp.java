row_sum = 0
cell_count = 0

for i in range(1, 4):
    for j in range(1, i + 2):
        row_sum = row_sum + (i * 10 + j)
        cell_count = cell_count + 1

print("Cell Count:", cell_count)
print("Row Sum:", row_sum)
