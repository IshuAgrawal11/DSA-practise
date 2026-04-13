nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 9
min_distance = float('inf')
for i in range(len(nums)):
    if nums[i] == target and abs(i - start) < min_distance:
        min_distance = abs(i - start)
print(min_distance)