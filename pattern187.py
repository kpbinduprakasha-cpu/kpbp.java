fruit = input()
length = len(fruit)
shuffle = ""

for i in range(length):
    index = int(input())
    shuffle = fruit[index] + shuffle

print(shuffle)
