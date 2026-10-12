a = int(input())

for i in range(1, a + 1):
    space = "  " * (a - i)
    row = "* " * (2 * i - 1)
    print(space + row)
