n = int(input())
count = 0
for i in range(n):
    for j in range(i):
        print("i:", i)
        print("j:", j)
        count = count + 1
        print("count:", count)
print(count)
