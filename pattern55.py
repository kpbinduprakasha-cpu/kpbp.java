a = int(input())
for i in range(1, a + 1):
    space = a - i
    start = " " * space
    star = "* " * i
    gap = " " * (2 * space)
    print(start + star + gap + star)
