a = int(input())

for i in range(1, a + 1):
    space = "  " * (i - 1)
    star = "* " * (a - i + 1)
    print(space + star)

for i in range(a - 1, 0, -1):
    space = "  " * (i - 1)
    star = "* " * (a - i + 1)
    print(space + star)
