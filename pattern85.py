a = int(input())

for i in range(1, a + 1):
    space = "  " * (a - i)

    if i == 1:
        print(space + "*")
    elif i == a:
        print("* " * (2 * a - 1))
    else:
        inner = "  " * (2 * i - 3)
        print(space + "*" + inner + "*")
