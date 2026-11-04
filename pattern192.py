a = int(input())
factor = 0
for i in range(2, a):
    if (a % i == 0):
        factor = factor + 1
if factor == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")
