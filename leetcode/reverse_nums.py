def minMirrorPairDistance(nums: list[int]) -> int:
    ans = 0
    found = False

    for i in range(len(nums)):
        num = int(str(nums[i])[::-1]) 
        for j in range(i + 1, len(nums)):
            if nums[j] == num:
                found = True
                if ans == 0:
                    ans = abs(i - j)
                else:
                    ans = min(ans, abs(i - j))
                break
    return ans if found else -1

       
nums1 = [12,21,45,33,54]
nums2 = [120,21]
nums3 = [2]
print(minMirrorPairDistance(nums1))
print(minMirrorPairDistance(nums2))
print(minMirrorPairDistance(nums3))

