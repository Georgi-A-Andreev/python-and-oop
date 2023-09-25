presents = int(input())
rows = int(input())

total_nice_kids = 0
total_nice_kids_with_presents = 0

matrix = []
santa = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for _ in range(rows):
    matrix.append(input().split())

for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == 'S':

            santa = [r, c]
        if matrix[r][c] == 'V':
            total_nice_kids += 1

while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[santa[0]][santa[1]] = '-'
    n_r, n_c = directions[command]
    r, c = n_r + santa[0], n_c + santa[1]

    if matrix[r][c] == 'X':
        santa = [r, c]
        matrix[santa[0]][santa[1]] = '-'
        matrix[r][c] = 'S'

    elif matrix[r][c] == 'V':
        total_nice_kids_with_presents += 1
        matrix[santa[0]][santa[1]] = '-'
        matrix[r][c] = 'S'
        santa = [r, c]
        presents -= 1

    elif matrix[r][c] == 'C':
        santa = [r, c]
        matrix[r][c] = 'S'
        for v in directions.values():
            row = santa[0]
            col = santa[1]
            row += v[0]
            col += v[1]

            if matrix[row][col] == 'V':
                matrix[row][col] = '-'
                total_nice_kids_with_presents += 1
                presents -= 1

            elif matrix[row][col] == 'X':
                matrix[row][col] = '-'
                presents -= 1

            if not presents:
                break
    else:
        matrix[santa[0]][santa[1]] = '-'
        matrix[r][c] = 'S'
        santa = [r, c]

    if not presents:
        break

if not presents and total_nice_kids - total_nice_kids_with_presents > 0:
    print(f"Santa ran out of presents!")
for el in matrix:
    print(' '.join(el))

if total_nice_kids_with_presents == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - total_nice_kids_with_presents} nice kid/s.")