def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
array = [5, 3, 2, 1, 4]
target = 2
result = linear_search(array, target)
print(result)

new = list(reversed(array))
print(new)

new2 = array[::-1]
print(new2)

array.reverse()
print(array)

list = [5,8,44,56,33,66,89]
start = 0
end = len(list) -1 
while start < end:
    list[start], list[end] = list[end], list[start]
    start += 1
    end -= 1
print(list)
