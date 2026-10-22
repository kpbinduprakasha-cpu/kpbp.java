# DSA Array: Reverse an array in-place using two-pointer approach
arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:
    # Swap elements at left and right indices
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed Array:", arr)
