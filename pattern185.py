a = int(input())
factoral = 0
for i in range(2, a):
    if (a % i) == 0:
        factoral = factoral + 1
if factoral == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")
