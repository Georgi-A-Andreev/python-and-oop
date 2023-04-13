field = []

for i in range(6):
    field.append(list(input().split()))

r, c = [int(i) for i in input() if i.isdigit()]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()

    if command == 'Stop':
        break

    co, *d = command.split(', ')
    r += directions[d[0]][0]
    c += directions[d[0]][1]

    if co == 'Create':
        if field[r][c] == '.':
            field[r][c] = d[1]

    elif co == 'Update':
        if field[r][c] != '.':
            field[r][c] = d[1]

    elif co == 'Delete':
        if field[r][c] != '.':
            field[r][c] = '.'

    elif co == 'Read':
        if field[r][c] != '.':
            print(field[r][c])

for i in field:
    print(' '.join(i))
