n = int(input())

for i in range(1, n + 1):
    spaces = "  " * (i - 1)

    if i == 1:
        print("* " * n)
    else:
        inner = "  " * (n - i)
        print(spaces + "* " + inner + ("*" if i < n else ""))
