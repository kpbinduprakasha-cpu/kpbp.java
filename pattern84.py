a = int(input())

for i in range(1, a + 1):
    space = "  " * (a - i)
    star = "* " * (2 * i - 1)
    print(space + star)

for i in range(a - 1, 0, -1):
    space = "  " * (a - i)
    star = "* " * (2 * i - 1)
    print(space + star)
