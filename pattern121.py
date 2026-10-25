n = int(input())
for i in range(1, n + 1):
    middel_space = (4 * n) - (4 * i - 1)
    holl_space = 2 * i - 3
    if i == 1:
        print("*" + " " * middel_space + "*")
    else:
        left = "*" + " " * holl_space + "*"
        right = "*" + " " * holl_space + "*"
        print(left + " " * middel_space + right)

for i in range(1, n + 1):
    middel_space = 4 * i - 3
    holl_space = 2 * (n - i) - 1

    if i == n:
        print("*" + " " * middel_space + "*")
    else:
        left = "*" + " " * holl_space + "*"
        right = "*" + " " * holl_space + "*"
        print(left + " " * middel_space + right)
