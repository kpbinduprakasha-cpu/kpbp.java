a = int(input())
b = int(input())

print("+" + "-" * b + "+")
for i in range(1, a + 2):
    if i > 1:
        print("|" + " " * b + "|")

print("+" + "-" * b + "+")
