rows = int(input())
cols = int(input())

areas = {}
visited = []
matrix = []
for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)


def dfs(el, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != el:
        return

    visited[row][col] = True
    dfs(el, row + 1, col, matrix, visited)
    dfs(el, row - 1, col, matrix, visited)
    dfs(el, row, col + 1, matrix, visited)
    dfs(el, row, col - 1, matrix, visited)

    return True


for row in range(rows):
    for col in range(cols):
        element = matrix[row][col]
        current = dfs(element, row, col, matrix, visited)
        if current is not None:
            if element not in areas:
                areas[element] = 0
            areas[element] += 1

print(f"Areas: {sum(areas.values())}")
for k, v in sorted(areas.items(), key=lambda x: x[0]):
    print(f"Letter '{k}' -> {v}")
