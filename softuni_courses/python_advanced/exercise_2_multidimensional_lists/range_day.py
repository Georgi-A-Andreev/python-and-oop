field = []
my_pos = []
shot_targets = 0
total_targets = 0
target_positions = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(5):
    field.append(input().split())
    if 'A' in field[r]:
        my_pos = [r, field[r].index('A')]
    if 'x' in field[r]:
        total_targets += field[r].count('x')

shots = int(input())
for i in range(shots):
    command, *data = input().split()

    if command == 'move':
        direction = data[0]
        steps = int(data[1])
        row, col = my_pos[0] + directions[direction][0] * steps, my_pos[1] + directions[direction][1] * steps
        if 0 <= row < 5 and 0 <= col < 5 and field[row][col] == '.':
            my_pos = [row, col]

    elif command == 'shoot':
        direction = data[0]
        row = my_pos[0]
        col = my_pos[1]
        while True:
            row += directions[direction][0]
            col += directions[direction][1]
            if 0 <= row < 5 and 0 <= col < 5:
                if field[row][col] == 'x':
                    field[row][col] = '.'
                    shot_targets += 1
                    target_positions.append([row, col])
                    break
            else:
                break
    if total_targets == shot_targets:
        break
if total_targets == shot_targets:
    print(f"Training completed! All {shot_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")

[print(i) for i in target_positions]
