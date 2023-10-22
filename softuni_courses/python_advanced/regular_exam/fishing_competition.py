rows = int(input())

our_position = (0, 0)
field = []
passages = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for _ in range(rows):
    field.append(list(input()))

for r in range(rows):
    for c in range(rows):
        if field[r][c] == 'S':
            our_position = (r, c)
            field[r][c] = '-'

while True:
    command = input()

    if command == 'collect the nets':
        break

    r = directions[command][0]
    c = directions[command][1]
    new_r = our_position[0] + r
    new_c = our_position[1] + c

    if command == 'up' and new_r == -1:
        new_r = rows - 1

    elif command == 'down' and new_r == rows:
        new_r = 0

    elif command == 'left' and new_c == -1:
        new_c = rows - 1

    elif command == 'right' and new_c == rows:
        new_c = 0

    if field[new_r][new_c].isdigit():
        passages += int(field[new_r][new_c])
        field[new_r][new_c] = '-'

    elif field[new_r][new_c] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{new_r},{new_c}]")
        quit()

    our_position = (new_r, new_c)

if passages >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota!", end=' ')
    print(f"You need {20 - passages} tons of fish more.")

if passages > 0:
    print(f"Amount of fish caught: {passages} tons.")

field[our_position[0]][our_position[1]] = 'S'
for el in field:
    print(''.join(el))
