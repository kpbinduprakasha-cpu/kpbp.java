count1 = 0
count2 = 14

for i in range(4, 6):
    for j in range(i):
        count1 = count1 + 1
    count2 = count2 - 1

print("Count2: " + str(count2))
print("Count1: " + str(count1))
