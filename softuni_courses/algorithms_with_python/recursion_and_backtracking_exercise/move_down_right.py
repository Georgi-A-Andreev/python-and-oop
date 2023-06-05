def move(field, rol, col, rows, cols, counter):
    if rol > rows or col > cols:
        return 0

    if rol == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += move(field, rol + 1, col, rows, cols, counter)
    result += move(field, rol, col + 1, rows, cols, counter)

    return result


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append([0] * cols)

print(move(matrix, 0, 0, rows, cols, 0))
