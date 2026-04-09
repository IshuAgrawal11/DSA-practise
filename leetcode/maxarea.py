height = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(height) - 1
max_area = 0
for i in range(len(height)):
    area = min(height[left], height[right]) * (right - left)
    max_area = max(max_area, area)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
print(max_area)