a = int(input())

for i in range(1, a + 1):
    space = "  " * (a - i)
    row = str(i) + " "
    row = row * i
    print(space + row)
