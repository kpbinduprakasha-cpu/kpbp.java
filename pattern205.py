a = int(input())
for i in range(a):
    space = "    " * i
    star = "* " * (2 * (a - i) - 1)
    print(space + star)
