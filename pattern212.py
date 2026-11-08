a = int(input())
k = a - 1
for i in range(1, a + 1):
    spaces = " " * k
    stars = "* " * i
    print(spaces + stars)
    k = k - 1
