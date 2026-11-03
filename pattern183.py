a = input()
length = len(a)
for i in range(1, length + 1):
    print(a[:i])
for i in range(length, 0, -1):
    print(a[:i])
