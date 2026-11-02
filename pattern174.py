a = input()
value = ""
for i in a:
    if i.isupper() and value != "":
        value = value + "-"
    value = value + i
print(value.lower())
