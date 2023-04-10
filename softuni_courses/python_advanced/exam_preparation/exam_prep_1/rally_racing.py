rows = int(input())
car_id = input()
field = []
car_position = [0, 0]
tunnel_positions = []
finish_position = []
total_km = 0
new_r = 0
new_c = 0

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

[field.append(input().split()) for _ in range(rows)]

for r in range(rows):
    for c in range(rows):
        if field[r][c] == 'T':
            tunnel_positions.append([r, c])

        elif field[r][c] == 'F':
            finish_position.append(r)
            finish_position.append(c)


while True:
    command = input()

    if command == 'End':
        print(f'Racing car {car_id} DNF.')
        break

    r, c = directions[command]
    new_r = car_position[0] + r
    new_c = car_position[1] + c

    if field[new_r][new_c] == '.':
        car_position = [new_r, new_c]
        total_km += 10

    elif field[new_r][new_c] == 'T':
        tunnel_positions.remove([new_r, new_c])
        car_position = tunnel_positions[0]
        field[new_r][new_c] = '.'
        field[car_position[0]][car_position[1]] = '.'
        total_km += 30

    elif field[new_r][new_c] == 'F':
        total_km += 10
        print(f'Racing car {car_id} finished the stage!')
        break

field[new_r][new_c] = 'C'
print(f'Distance covered {total_km} km.')
[print(''.join(i)) for i in field]
