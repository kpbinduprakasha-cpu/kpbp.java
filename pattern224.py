n = int(input())
for i in range(1, n + 1):
    row = ""
    for j in range(i):
        row = row + chr(65 + j) + " "
    print(row)
