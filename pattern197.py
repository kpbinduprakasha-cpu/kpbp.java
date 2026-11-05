M = int(input())
N = int(input())

row = ""
for k in range(1, N + 1):
    row = row + (str(k) + " ")

for i in range(M):
    print(row)
