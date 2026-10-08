a = int(input())
coutn = 0
for i in range(a):
    space = ("  ") * (a - i - 1)
    stars = ("* ") * ((2 * i) + 1)
    print(space + stars)
