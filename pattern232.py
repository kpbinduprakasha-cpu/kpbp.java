n = int(input())
for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == 1 or i == n:
        print(spaces + "* " * i)
    else:
        inner_spaces = "  " * (i - 2)
        print(spaces + "* " + inner_spaces + "* ")
