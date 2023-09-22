rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    if command[0] != 'swap':
        print('Invalid input!')
        continue

    if len(command[1:]) == 4:
        row, col, row1, col1 = [int(x) for x in command[1:]]
        if row > rows or row1 > rows or col > cols or col1 > cols:
            print('Invalid input!')
        else:
            matrix[row][col], matrix[row1][col1] = matrix[row1][col1], matrix[row][col]
            for el in matrix:
                print(*el)
                continue
    else:
        print('Invalid input!')
