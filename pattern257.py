word1 = "Hello"
word2 = "CCBPian"
count = 0

for a in word1:
    for b in word2:
        if a == b:
            count = count + 1

print(count)
