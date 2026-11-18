class solution:
    def largestElement(self, arr, n):
        largest=arr[0]
        for i in range(1,len(arr)):
            if largest<arr[i]:
                largest=arr[i]
        return largest
