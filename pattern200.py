a = input()
result = ""

for i in range(len(a)):
    if a[i].isupper() and i != 0:
        result = result + "-"
    result = result + a[i].lower()

print(result)
