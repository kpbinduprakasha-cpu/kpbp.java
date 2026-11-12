diag_sum = 0
off_sum = 0

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            diag_sum = diag_sum + (i * j)
        else:
            off_sum = off_sum + (i + j)

print("Diagonal:", diag_sum)
print("Off-diagonal:", off_sum)
