n = int(input())

for i in range(n):
    spaces = "  " * i
    stars = "* " * (n - i)
    print(spaces + stars)
