rows, cols = [int(x) for x in input().split()]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

field = []
starting_position = [0, 0]
end_position = [0, 0]

for _ in range(rows):
    field.append(list(input()))

for r in range(rows):
    for c in range(cols):
        if field[r][c] == 'B':
            starting_position = [r, c]
            end_position = [r, c]

while True:
    command = input()
    new_row, new_col = directions[command]
    row, col = starting_position[0] + new_row, starting_position[1] + new_col

    if row >= len(field) or col >= len(field[0]) or row < 0 or col < 0:
        print("The delivery is late. Order is canceled.")
        field[end_position[0]][end_position[1]] = ' '
        break

    elif field[row][col] == 'R':
        starting_position[0] += new_row
        starting_position[1] += new_col
        continue

    elif field[row][col] == 'P':
        field[row][col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        starting_position[0] += new_row
        starting_position[1] += new_col
        continue

    elif field[row][col] == '*':
        continue

    elif field[row][col] == 'A':
        field[row][col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

    field[row][col] = '.'
    starting_position[0] += new_row
    starting_position[1] += new_col

if field[end_position[0]][end_position[1]] == '.':
    field[end_position[0]][end_position[1]] = 'B'

for el in field:
    print(''.join(el))
