a = int(input())

for i in range(1, a + 1):
    value = a - i
    space = "  " * value
    row = "* " * i
    print(space + row)
