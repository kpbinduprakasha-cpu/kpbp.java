a = int(input())
b = int(input())
for i in range(1, a + 1):
    if i % 2 == 1:
        print("+ " * b)
    if i % 2 == 0:
        print("- " * b)
