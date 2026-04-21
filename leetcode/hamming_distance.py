def minimumHammingDistance(source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        count = 0

        for i in range(len(source)):
            for j in range(i+1, len(source)):
                if [i, j] in allowedSwaps or [j, i] in allowedSwaps:
                    source[i], source[j] = source[j], source[i]

        for i in range(len(source)):
            if source[i] != target[i]:
                count += 1
        return count

source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
print(minimumHammingDistance(source, target, allowedSwaps))