a = input()
n = len(a)
shuffled_a = ""
for i in range(n):
    index = int(input())
    shuffled_a = shuffled_a + a[index]
print(shuffled_a)
