rows, cols = [int(x) for x in input().split()]

matrix = []
result = 0
for _ in range(rows):
    matrix.append(input().split())

for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            result += 1

print(result)
