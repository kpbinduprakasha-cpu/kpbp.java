n = int(input())
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            row = row + "1 "
        else:
            row = row + "0 "
    print(row)
