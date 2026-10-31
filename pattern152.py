string = input()

start_index = 2
step = 3
word = ""

for i in range(start_index, len(string), step):
    word = word + string[i]

print(word)
