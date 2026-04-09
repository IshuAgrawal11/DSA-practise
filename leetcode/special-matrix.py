mat = [[1,0,0],[0,0,1],[1,0,0]]
row_sums = [sum(row) for row in mat]
col_sums = [sum(col) for col in zip(*mat)]

count = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            if row_sums[i] == 1 and col_sums[j] == 1:
                count += 1

print(count)

# second approach

def numSpecial(self, mat: list[list[int]]) -> int:
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        count = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                count += get_column_sum(col_idx) == 1

        return count
        