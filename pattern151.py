text = input()
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(count)
