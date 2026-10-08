a = int(input())
for i in range(1,a+1):
    print("  " * (a - i) + (str(i) + " ") * (2 * i - 1))
