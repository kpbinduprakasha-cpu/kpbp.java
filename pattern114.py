# DSA Array: Check if an array is sorted in ascending order
arr = [1, 3, 5, 7, 9, 11]

is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("The array is sorted.")
else:
    print("The array is not sorted.")
