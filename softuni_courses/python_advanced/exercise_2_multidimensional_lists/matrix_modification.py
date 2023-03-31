rows = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

while True:
    command, *data = input().split()

    if command == 'END':
        break

    row = int(data[0])
    col = int(data[1])
    new = int(data[2])

    if 0 <= row < rows and 0 <= col < rows:
        if command == 'Add':
            matrix[row][col] += new
        elif command == 'Subtract':
            matrix[row][col] -= new
    else:
        print('Invalid coordinates')

[print(*i) for i in matrix]
