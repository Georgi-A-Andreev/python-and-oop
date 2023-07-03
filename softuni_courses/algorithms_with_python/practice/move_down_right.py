rows = int(input())
cols = int(input())
counter = 0
field = []
for _ in range(rows):
    field.append([None] * cols)


def find_all_paths(field, row, col):
    if row >= len(field) or col >= len(field[0]):
        return 0
    if row == len(field) - 1 and col == len(field[0]) - 1:
        return 1
    result = 0
    result += find_all_paths(field, row + 1, col)
    result += find_all_paths(field, row, col + 1)

    return result


print(find_all_paths(field, 0, 0))
