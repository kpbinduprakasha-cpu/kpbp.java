a = input()
value = ""
for i in a:
    if i not in "AEIOUaeiou":
        value = value + i
print(value)
