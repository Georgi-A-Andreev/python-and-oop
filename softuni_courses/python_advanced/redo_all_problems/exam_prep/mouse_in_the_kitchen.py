rows, cols = [int(x) for x in input().split(',')]

total_cheese = 0
mouse_position = [0, 0]
field = []

for _ in range(rows):
    field.append(list(input()))

for r in range(rows):
    for c in range(cols):
        if field[r][c] == 'M':
            field[r][c] = '*'
            mouse_position = [r, c]
        if field[r][c] == 'C':
            total_cheese += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()

    if command == 'danger':
        field[mouse_position[0]][mouse_position[1]] = 'M'
        print("Mouse will come back later!")
        break

    new_row = directions[command][0]
    new_col = directions[command][1]

    row = mouse_position[0] + new_row
    col = mouse_position[1] + new_col

    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        field[mouse_position[0]][mouse_position[1]] = 'M'
        print("No more cheese for tonight!")

        break

    if field[row][col] == '@':
        continue

    if field[row][col] == '*':
        mouse_position[0] = row
        mouse_position[1] = col
        continue

    if field[row][col] == 'C':
        field[row][col] = '*'
        mouse_position[0] = row
        mouse_position[1] = col
        total_cheese -= 1
        if total_cheese == 0:
            field[row][col] = 'M'
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    if field[row][col] == 'T':
        print("Mouse is trapped!")
        field[row][col] = 'M'
        break

for el in field:
    print(''.join(el))