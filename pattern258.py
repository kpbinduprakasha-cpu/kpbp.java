i = 1
total = 0

while (i < 3):
    j = 1
    while (j < 3):
        if((i ** j) < 6):
            total = total + 1
        j = j + 1
    i = i + 1

print(total)
