a = int(input())

count = int(input())

for i in range(1, a):
    b = int(input())

    if b < count:
        count = b

print(count)
