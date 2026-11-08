inner = 6
outer = 6

for i in range(6, 7):
    for j in range(i):
        inner = inner - 1
    outer = outer - 1

print("Outer: " + str(outer))
print("Inner: " + str(inner))
