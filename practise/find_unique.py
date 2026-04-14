def findUnique(arr:list[int], n:int) -> int:
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
    return -1
    #write your code here 
arr = [2, 3, 1, 6, 3, 6, 2]
n = len(arr)
print(findUnique(arr, n))


# SECOND APPROACH
def Unique(arr):
    counts = {}
    
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    for key, value in counts.items():
        if value == 1:
            return key
            
    return -1

print(Unique(arr))

# opttimised approach
def findUnique(arr):
    unique = 0
    for num in arr:
        unique ^= num
    #write your code here
    return unique 
