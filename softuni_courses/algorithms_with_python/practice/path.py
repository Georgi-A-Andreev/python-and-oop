rows = int(input())
cols = int(input())

field = []
for _ in range(rows):
    field.append(list(input()))


def find_all_paths(rows, cols, field, row, col, direction, path):
    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return
    if field[row][col] == '*':
        return
    if field[row][col] == 'v':
        return
    if field[row][col] == 'e':
        path.append(direction)
        print(''.join(path))
        path.pop()
        return

    field[row][col] = 'v'
    path.append(direction)
    find_all_paths(rows, cols, field, row, col + 1, 'R', path)
    find_all_paths(rows, cols, field, row, col - 1, 'L', path)
    find_all_paths(rows, cols, field, row + 1, col, 'D', path)
    find_all_paths(rows, cols, field, row - 1, col, 'U', path)
    field[row][col] = '-'
    path.pop()


find_all_paths(rows, cols, field, 0, 0, '', [])
