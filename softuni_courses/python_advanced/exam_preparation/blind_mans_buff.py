rows, cols = [int(x) for x in input().split()]
my_position = []
field = []
total_moves = 0
touched_opponents = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(rows):
    field.append(list(input().split()))

for r in range(rows):
    for c in range(cols):
        if field[r][c] == 'B':
            my_position = [r, c]

while True:
    command = input()
    if command == 'Finish':
        break

    r, c = my_position[0] + directions[command][0], my_position[1] + directions[command][1]

    if 0 <= r < rows and 0 <= c < cols:
        if field[r][c] == 'O':
            continue

        elif field[r][c] == '-':
            pass

        elif field[r][c] == 'P':
            field[r][c] = '-'
            touched_opponents += 1

        total_moves += 1
        my_position = [r, c]

    if touched_opponents == 3:
        break

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {total_moves}')
