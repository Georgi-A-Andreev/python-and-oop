rows, cols = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

best_square = (0, 0)
best_sum = float('-inf')

for r in range(rows - 2):
    for c in range(cols - 2):
        current_sum = 0
        for i in range(3):
            current_sum += sum([matrix[r + i][c], matrix[r + i][c + 1], matrix[r + i][c + 2]])

        if current_sum > best_sum:
            best_sum = current_sum
            best_square = (r, c)
print(f'Sum = {best_sum}')
row = best_square[0]
col = best_square[1]

for r in range(row, row + 3):
    for c in range(col, col + 3):
        print(matrix[r][c], end=' ')
    print()
