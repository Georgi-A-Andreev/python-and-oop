rows = int(input())

field = []
result = 0
directions = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]

for _ in range(rows):
    field.append(list(input()))

while True:
    current_best_knight = 0
    current_best_knight_coordinates = ()

    for row in range(rows):
        for col in range(rows):
            current = 0
            if field[row][col] == '0':
                continue
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if 0 <= new_row < rows and 0 <= new_col < rows and field[new_row][new_col] == 'K':
                    current += 1

            if current > current_best_knight:
                current_best_knight = current
                current_best_knight_coordinates = (row, col)

    if current_best_knight:
        field[current_best_knight_coordinates[0]][current_best_knight_coordinates[1]] = '0'
        result += 1
    else:
        print(result)
        break
