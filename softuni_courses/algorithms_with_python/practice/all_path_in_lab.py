rows = int(input())
cols = int(input())

lab = []
[lab.append(list(input())) for _ in range(rows)]


def gen_paths(lab, rows, cols, row, col, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return
    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    else:

        lab[row][col] = 'v'

        gen_paths(lab, rows, cols, row - 1, col, 'U', path)
        gen_paths(lab, rows, cols, row + 1, col, 'D', path)
        gen_paths(lab, rows, cols, row, col - 1, 'L', path)
        gen_paths(lab, rows, cols, row, col + 1, 'R', path)
        lab[row][col] = '-'
    path.pop()


gen_paths(lab, rows, cols, 0, 0, '', [])