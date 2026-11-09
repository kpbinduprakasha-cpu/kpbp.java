n = int(input())
total = n * (n + 1) // 2
for i in range(n, 0, -1):
    row = ""
    for j in range(i):
        row = row + str(total) + " "
        total = total - 1
    print(row)
