s = int(input())
n = int(input())

first_row = ""

for row in range(n):
    first_row = first_row + str(s + row) + " "

for row in range(n):
    print(first_row)
