rows = int(input())

field = [input().split() for _ in range(rows)]
alice = []
rabit = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    for col in range(rows):
        if field[row][col] == 'A':
            alice = [row, col]
            field[row][col] = '*'
        if field[row][col] == 'R':
            rabit = [row, col]

tea = 0
did_it = False
while True:
    command = input()

    r, c = directions[command][0], directions[command][1]
    alice[0] += r
    alice[1] += c
    row, col = alice[0], alice[1]
    if row < 0 or col < 0 or row >= rows or col >= rows:
        break
    if field[row][col] == 'R':
        field[row][col] = '*'
        break
    if field[row][col] != '.' and field[row][col] != '*':
        tea += int(field[row][col])

    field[row][col] = '*'

    if tea >= 10:
        did_it = True
        break

if did_it:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for el in field:
    print(*el, sep=' ')
