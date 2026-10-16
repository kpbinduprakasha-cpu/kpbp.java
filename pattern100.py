target = 3
current = 1

while current <= 5:
    if current == target:
        print(f"Found the target: {target}!")
        break  
    current += 1
else:
    print("Searched all numbers but didn't find the target.")
