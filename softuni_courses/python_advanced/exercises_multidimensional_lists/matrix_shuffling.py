rol, col = [int(x) for x in input().split()]

matrix = [input().split() for x in range(rol)]

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    if command[0] == 'swap' and len(command) == 5:
        x1, y1, x2, y2 = [int(i) for i in command[1:5]]
        if 0 <= x1 < rol and 0 <= x2 < rol and 0 <= y1 < col and 0 <= y2 < col:
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            [print(*i) for i in matrix]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
