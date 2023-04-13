from collections import deque

field = []
rover = []
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for _ in range(6):
    field.append(input().split())

for r in range(6):
    for c in range(6):
        if field[r][c] == 'E':
            rover = [r, c]

commands = deque(input().split(', '))

while commands:
    new_r, new_c = directions[commands.popleft()]
    rover = [rover[0] + new_r, rover[1] + new_c]
    rover[0] = 5 if rover[0] == -1 else rover[0]
    rover[0] = 0 if rover[0] == 6 else rover[0]
    rover[1] = 5 if rover[1] == -1 else rover[1]
    rover[1] = 0 if rover[1] == 6 else rover[1]

    if field[rover[0]][rover[1]] == 'W':
        water_deposit += 1
        print(f'Water deposit found at ({rover[0]}, {rover[1]})')

    elif field[rover[0]][rover[1]] == 'M':
        metal_deposit += 1
        print(f'Metal deposit found at ({rover[0]}, {rover[1]})')

    elif field[rover[0]][rover[1]] == 'C':
        concrete_deposit += 1
        print(f'Concrete deposit found at ({rover[0]}, {rover[1]})')

    elif field[rover[0]][rover[1]] == 'R':
        print(f'Rover got broken at ({rover[0]}, {rover[1]})')
        break

if all([water_deposit, concrete_deposit, metal_deposit]):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
