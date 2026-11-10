n = int(input())
a, b = 0, 1
sequence = ""
for i in range(n):
    sequence = sequence + str(a) + " "
    a, b = b, a + b
print(sequence)
