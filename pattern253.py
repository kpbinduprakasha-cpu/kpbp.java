balance = 0

for i in range(1, 4):
    for j in range(1, 5):
        if (i + j) % 2 == 0:
            balance = balance + j
        else:
            balance = balance - i

print(balance)
