def maxDistance(colors):
    n = len(colors)
    max_dist = 0
    
    # Scenario 1: Distance from the first house (index 0)
    for i in range(n - 1, -1, -1):
        if colors[i] != colors[0]:
            max_dist = max(max_dist, i)
            break
            
    # Scenario 2: Distance from the last house (index n-1)
    for i in range(n):
        if colors[i] != colors[n - 1]:
            max_dist = max(max_dist, (n - 1) - i)
            break
            
    return max_dist

# Test
colors = [1, 1, 1, 6, 1, 1, 1]
print(maxDistance(colors)) # Output: 3 (index 0 to index 3)