def check_for_areas(value, row, col, matrix, areas, visited_fields):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if visited_fields[row][col]:
        return 0
    if matrix[row][col] != value:
        return 0

    if value not in areas:
        areas[value] = 0

    visited_fields[row][col] = True

    check_for_areas(value, row + 1, col, matrix, areas, visited_fields)
    check_for_areas(value, row - 1, col, matrix, areas, visited_fields)
    check_for_areas(value, row, col + 1, matrix, areas, visited_fields)
    check_for_areas(value, row, col - 1, matrix, areas, visited_fields)

    return 1


rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

areas = {}
visited_fields = []


for _ in range(rows):
    visited_fields.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if check_for_areas(matrix[row][col], row, col, matrix, areas, visited_fields) == 1:
            areas[matrix[row][col]] += 1

print(f"Areas: {sum(areas.values())}")
for k in sorted(areas, key=lambda x: x):
    print(f"Letter '{k}' -> {areas[k]}")
