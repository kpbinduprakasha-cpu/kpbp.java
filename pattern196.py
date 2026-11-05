a = int(input())
for i in range(1, a + 3):
    if i == 1 or i == (a + 2):
        hyphens = ("- ") * a
        row = "+ " + hyphens + "+"
    else:
        spaces = ("  ") * a
        row = "| " + spaces + "|"
    print(row)
