def find_areas(element, row, col, matrix, visited):
    if row >= len(matrix) or row < 0 or col >= len(matrix[0]) or col < 0:
        return
    if visited[row][col]:
        return
    if matrix[row][col] != element:
        return
    visited[row][col] = True
    find_areas(element, row + 1, col, matrix, visited)
    find_areas(element, row - 1, col, matrix, visited)
    find_areas(element, row, col + 1, matrix, visited)
    find_areas(element, row, col - 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []
[visited.append([False] * cols) for _ in range(rows)]
areas = {}

for _ in range(rows):
    matrix.append(list(input()))

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        element = matrix[row][col]
        find_areas(element, row, col, matrix, visited)
        if element not in areas:
            areas[element] = 0
        areas[element] += 1

print(f"Areas: {sum(areas.values())}")
for k, v in sorted(areas.items(), key=lambda x: x):
    print(f"Letter '{k}' -> {v}")
