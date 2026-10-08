a = int(input())
value = 0
for i in range(1, a + 1):
    number = (a + 1) - i
    space = (" ") * (i - 1)
    print(space + str(number) * number)
