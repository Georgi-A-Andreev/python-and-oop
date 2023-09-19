rows, cols = [int(x) for x in input().split(', ')]
matrix = []
best_sum = float('-inf')
best_sum_index = (0, 0)
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1] > best_sum:
            best_sum_index = (r, c)
            best_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]

print(matrix[best_sum_index[0]][best_sum_index[1]], matrix[best_sum_index[0]][best_sum_index[1] + 1])
print(matrix[best_sum_index[0] + 1][best_sum_index[1]], matrix[best_sum_index[0] + 1][best_sum_index[1] + 1])
print(best_sum)
