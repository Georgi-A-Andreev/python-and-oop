rows = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

bunny_pos = []
best_direction = None
most_eggs = 0
result_end = []
field = [input().split() for _ in range(rows)]

for r in range(rows):
    for c in range(rows):
        if field[r][c] == 'B':
            bunny_pos = [r, c]

for direction, move in directions.items():
    b_r = bunny_pos[0]
    b_c = bunny_pos[1]
    current_eggs = 0

    result = []
    while True:
        b_r += move[0]
        b_c += move[1]
        if 0 <= b_r < rows and 0 <= b_c < rows and field[b_r][b_c] != 'X':
            current_eggs += int(field[b_r][b_c])
            result.append([b_r, b_c])
        else:
            break
    if current_eggs >= most_eggs:
        most_eggs = current_eggs
        best_direction = direction
        result_end = result

print(best_direction)
print(*result_end, sep='\n')
print(most_eggs)
