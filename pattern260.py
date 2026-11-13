pattern = ""

for i in range(3, 4):
    pattern = ""
    for j in range(1, i + 1):
        if(j == i):
            pattern = pattern + str(j)
        else:
            pattern = pattern + str(j) + " "
print(pattern)
