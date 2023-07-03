rows = int(input())
cols = int(input())
areas = {}
matrix = []
for _ in range(rows):
    matrix.append(list(input()))


def find_all_areas(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '-':
        return 0
    result = 1
    matrix[row][col] = 'v'
    result += find_all_areas(matrix, row + 1, col)
    result += find_all_areas(matrix, row - 1, col)
    result += find_all_areas(matrix, row, col + 1)
    result += find_all_areas(matrix, row, col - 1)

    return result


for row in range(rows):
    for col in range(cols):
        result = find_all_areas(matrix, row, col)

        if result != 0:
            areas[(row, col)] = result

print(f'Total areas found: {len(areas)}')
for p, (k, v) in enumerate(sorted(areas.items(), key=lambda x: -x[1])):
    print(f'Area #{p + 1} at {k}, size: {v}')
