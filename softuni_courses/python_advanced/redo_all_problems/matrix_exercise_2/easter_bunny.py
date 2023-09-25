rows = int(input())
field = []
bunny = []

directions = {
    (0, -1): 'left',
    (0, 1): 'right',
    (1, 0): 'down',
    (-1, 0): 'up'
}

for _ in range(rows):
    field.append(input().split())

for r in range(rows):
    for c in range(rows):
        if field[r][c] == 'B':
            bunny = [r, c]

best_positions = []
best_direction = ''
total_eggs = float('-inf')
for k, v in directions.items():
    row = bunny[0]
    col = bunny[1]
    current = 0
    current_steps = []
    while True:
        row += k[0]
        col += k[1]
        if 0 <= row < rows and 0 <= col < rows and field[row][col] != 'X':
            current += int(field[row][col])
            current_steps.append([row, col])
        else:
            break
    if current >= total_eggs:
        total_eggs = current
        best_direction = v
        best_positions = current_steps

print(best_direction)
print(*best_positions, sep='\n')
print(total_eggs)
