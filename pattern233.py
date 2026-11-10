n = int(input())
for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == 1:
        print(spaces + "*")
    else:
        inner_spaces = " " * (2 * i - 3)
        print(spaces + "*" + inner_spaces + "*")
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    if i == 1:
        print(spaces + "*")
    else:
        inner_spaces = " " * (2 * i - 3)
        print(spaces + "*" + inner_spaces + "*")
