a = int(input())

for i in range(a, 0, -1):
    space = "  " * (a - i)
    row = ""

    for j in range(1, i + 1):
        row = row + str(j) + " "

    print(space + row)
