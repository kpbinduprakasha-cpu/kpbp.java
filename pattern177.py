a = input()
value = ""
for i in a:
    if i != " " and i != "'" and i != '"':
        value = value + i
revers = value[::-1]
if value.lower() == revers.lower():
    print("True")
else:
    print("False")
