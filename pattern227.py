n = int(input())
for i in range(1, n + 1):
    spaces = "  " * (n - i)
    left = ""
    for j in range(1, i + 1):
        left = left + str(j) + " "
    right = ""
    for j in range(i - 1, 0, -1):
        right = right + str(j) + " "
    print(spaces + left + right)
