def distance(nums: list[int]) -> list[int]:
    ans =[]
    for i in range(len(nums)):
        temp = 0
        for j in range(len(nums)):
            if nums[i] == nums[j] and i != j:
                temp += abs(i-j)
        ans.append(temp)
    return ans
       

nums = [1,3,1,1,2]
print(distance(nums))

def distance(nums: list[int]) -> list[int]:
    ans =[]
    for i in range(len(nums)):
        temp = 0
        count = 0
        while count < len(nums):
            if nums[i] == nums[count] and i != count and count < len(nums):
                temp += abs(i-count)
            count += 1
        ans.append(temp)
    return ans
       

nums = [1,3,1,1,2]
print(distance(nums))