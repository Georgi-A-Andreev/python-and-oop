rows = int(input())
battlefield = []
submarine_position = []
submarine_health = 3
cruisers = 3

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(rows):
    battlefield.append(list(input()))

for r in range(rows):
    for c in range(rows):
        if battlefield[r][c] == 'S':
            submarine_position = [r, c]

while True:
    r_change, c_change = directions[input()]
    battlefield[submarine_position[0]][submarine_position[1]] = '-'
    r, c = submarine_position[0] + r_change, submarine_position[1] + c_change
    submarine_position = [r, c]

    if battlefield[r][c] == '-':
        continue

    elif battlefield[r][c] == '*':
        submarine_health -= 1
        if submarine_health == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates "
                  f"[{submarine_position[0]}, {submarine_position[1]}]!")
            break

    elif battlefield[r][c] == 'C':
        cruisers -= 1
        if cruisers == 0:
            print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

    battlefield[r][c] = '-'

battlefield[r][c] = 'S'
[print(''.join(i)) for i in battlefield]
