array = [5, 8, 44, 56, 33, 66, 89]
start = 0
end = start + 1
for i in range(0, len(array) - 1, 2):
    array[start], array[end] = array[end], array[start]
    start += 2
    end += 2
print(array)