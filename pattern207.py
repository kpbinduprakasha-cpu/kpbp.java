a = int(input())
count = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        count = count + i
print(count)
