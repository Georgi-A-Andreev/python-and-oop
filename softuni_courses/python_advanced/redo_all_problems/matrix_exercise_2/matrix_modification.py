rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command_str = input()

    if command_str == 'END':
        for el in matrix:
            print(*el)
        break

    command, row_str, col_str, value_str = command_str.split()
    row, col, value = int(row_str), int(col_str), int(value_str)

    if row < 0 or row >= rows or col < 0 or col >= rows:
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][col] += value

    elif command == 'Subtract':
        matrix[row][col] -= value
