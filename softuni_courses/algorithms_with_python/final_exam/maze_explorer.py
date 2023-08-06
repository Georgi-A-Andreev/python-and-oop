def find_path(row, col, field, best_path, current_best):
    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return
    if field[row][col] == '#':
        return
    if field[row][col] == 'v':
        return
    if field[row][col] == 'E':
        best_path.append(current_best)
        return

    field[row][col] = 'v'
    current_best += 1

    find_path(row + 1, col, field, best_path, current_best)
    find_path(row - 1, col, field, best_path, current_best)
    find_path(row, col + 1, field, best_path, current_best)
    find_path(row, col - 1, field, best_path, current_best)

    current_best -= 1
    field[row][col] = '.'


rows = int(input())

field = []
[field.append(list(input())) for _ in range(rows)]

paths = []
find_path(0, 0, field, paths, 0)
print(min(paths))
