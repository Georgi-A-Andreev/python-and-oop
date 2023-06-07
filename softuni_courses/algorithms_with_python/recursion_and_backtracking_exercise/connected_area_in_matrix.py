def find_areas(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'
    result = 1
    result += find_areas(matrix, row - 1, col)
    result += find_areas(matrix, row + 1, col)
    result += find_areas(matrix, row, col - 1)
    result += find_areas(matrix, row, col + 1)

    return result

rows = int(input())
cols = int(input())

matrix = []

for i in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        result = find_areas(matrix, row, col)
        if result == 0:
            continue

        areas.append((row, col, result))
areas = sorted(areas, key=lambda x: -x[-1])
print(f'Total areas found: {len(areas)}')
for i in range(1, len(areas) + 1):
    print(f"Area #{i} at ({areas[i - 1][0]}, {areas[i - 1][1]}), size: {areas[i - 1][-1]}")
