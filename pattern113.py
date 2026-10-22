# DSA Array: Move all zeroes to the end of the array while maintaining order
arr = [0, 1, 0, 3, 12]

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print("Array after moving zeroes:", arr)
