size = int(input("Enter the size of the array: "))
arr = list(map(int, input().split()))
arr = arr[:size]
print("Array so far: ", arr)

def getMax(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def getMin(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

print("Maximum element: ", getMax(arr))
print("Minimum element: ", getMin(arr))


