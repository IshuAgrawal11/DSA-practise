nums = [1,3,1,4,1,3,2]
queries = [0,3,5]
array = []
for query in queries:
    for i in range(len(nums)):
        if nums[query] == nums[i]:
            distance = abs(nums.index(nums[query]) - nums.index(nums[i]))
            array.append(distance)
            break
        else:
            array.append(-1)
            break
print(array)