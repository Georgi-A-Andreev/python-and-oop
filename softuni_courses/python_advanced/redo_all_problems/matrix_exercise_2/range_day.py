field = [input().split() for _ in range(5)]
our_pos = []

directions = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}

total_targets = 0
for r in range(5):
    for c in range(5):
        if field[r][c] == 'A':
            our_pos = [r, c]
        if field[r][c] == 'x':
            total_targets += 1

commands_count = int(input())
shot_targets = 0
target_locations = []

for _ in range(commands_count):
    command = input().split()
    d_r = directions[command[1]][0]
    d_c = directions[command[1]][1]

    if command[0] == 'move':
        new_r = our_pos[0] + (d_r * int(command[2]))
        new_c = our_pos[1] + (d_c * int(command[2]))
        if 0 <= new_r < 5 and 0 <= new_c < 5 and field[new_r][new_c] == '.':
            our_pos = [new_r, new_c]

    elif command[0] == 'shoot':
        current_row = our_pos[0]
        current_col = our_pos[1]
        while True:
            current_row += d_r
            current_col += d_c
            if current_row < 0 or current_col < 0 or current_row >= 5 or current_col >= 5:
                break
            if field[current_row][current_col] == 'x':
                field[current_row][current_col] = '.'
                shot_targets += 1
                target_locations.append([current_row, current_col])
                break
    if shot_targets == total_targets:
        break
if shot_targets == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")

print(*target_locations, sep='\n')
