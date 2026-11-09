n = int(input())
for i in range(n):
    spaces = " " * (n - i)
    row = ""
    val = 1
    for j in range(i + 1):
        row = row + str(val) + " "
        val = val * (i - j) // (j + 1)
    print(spaces + row)
