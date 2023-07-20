rows = int(input())
cols = int(input())


def find_all_paths(rows, cols, row, col):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += find_all_paths(rows, cols, row + 1, col)
    result += find_all_paths(rows, cols, row, col + 1)

    return result


print(find_all_paths(rows, cols, 0, 0))