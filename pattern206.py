a = input()
a_length = len(a)
b = input()
value = ""
for i in range(a_length):
    if i % 2 == 0:
        value = value + a[i]
    if i % 2 == 1:
        value = value + b[i]
print(value)
