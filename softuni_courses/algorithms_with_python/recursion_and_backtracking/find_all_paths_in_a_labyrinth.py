def find_path(field, rows, cols, direction, path):

    if rows < 0 or rows >= len(field) or cols < 0 or cols >= len(field[0]):

        return

    if field[rows][cols] == 'e':
        path.append(direction)
        print(''.join(path))
        path.pop()
        return

    if field[rows][cols] != '-':
        return

    field[rows][cols] = 'v'
    path.append(direction)

    find_path(field, rows, cols + 1, 'R', path)
    find_path(field, rows, cols - 1, 'L', path)
    find_path(field, rows + 1, cols, 'D', path)
    find_path(field, rows - 1, cols, 'U', path)

    path.pop()
    field[rows][cols] = '-'


rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
    matrix.append(list(input()))

find_path(matrix, 0, 0, '', [])
