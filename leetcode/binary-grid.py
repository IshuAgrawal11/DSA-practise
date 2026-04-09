def minSwaps(grid: list[list[int]]) -> int:
    n = len(grid)
    trailing_zeroes = []
    for row in grid:
        count = 0
        for j in range(n - 1, -1, -1):
            if row[j] == 0:
                count += 1
            else:
                break
        trailing_zeroes.append(count)
    steps = 0
    for i in range(n):
        found = -1
        target = n - 1 - i
        for j in range(i, n):
            if trailing_zeroes[j] >= target:
                found = j
                break
        if found == -1:
            return -1
        current_value = trailing_zeroes.pop(found)
        trailing_zeroes.insert(i, current_value)

        steps += (found - i)
    return steps
        

# Example usage:
grid = [[0,0,1],[1,1,0],[1,0,0]]
print(minSwaps(grid))