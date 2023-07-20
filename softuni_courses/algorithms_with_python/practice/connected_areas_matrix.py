rows = int(input())
cols = int(input())
areas = {}
field = []

for _ in range(rows):
    field.append(list(input()))


def find_all_areas(field, row, col):
    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return 0
    if field[row][col] == 'v':
        return 0
    if field[row][col] == '*':
        return 0
    field[row][col] = 'v'

    result = 1
    result += find_all_areas(field, row + 1, col)
    result += find_all_areas(field, row - 1, col)
    result += find_all_areas(field, row, col + 1)
    result += find_all_areas(field, row, col - 1)

    return result


for row in range(rows):
    for col in range(cols):
        area = find_all_areas(field, row, col)

        if area != 0:
            areas[(row, col)] = area

print(f'Total areas found: {len(areas)}')
counter = 1
for k, v in sorted(areas.items(), key=lambda x: -x[1]):
    print(f'Area #{counter} at {k}, size: {v}')
    counter += 1
