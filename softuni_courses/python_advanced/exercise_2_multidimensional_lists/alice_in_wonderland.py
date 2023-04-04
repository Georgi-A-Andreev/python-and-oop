rows = int(input())
field = []
alice_position = []
tea_bags = 0
walked_path = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


for i in range(rows):
    field.append(input().split())
    if 'A' in field[i]:
        alice_position = [i, field[i].index('A')]
        field[i][field[i].index('A')] = '*'

while tea_bags < 10:
    command = input()
    row_change, col_change = directions[command]
    alice_position[0] += row_change
    alice_position[1] += col_change

    if not (0 <= alice_position[0] < rows and 0 <= alice_position[1] < rows):
        print("Alice didn't make it to the tea party.")
        break
    elif field[alice_position[0]][alice_position[1]] == 'R':
        walked_path.append([alice_position[0], alice_position[1]])
        print("Alice didn't make it to the tea party.")
        break
    else:
        if field[alice_position[0]][alice_position[1]].isdigit():
            tea_bags += int(field[alice_position[0]][alice_position[1]])
        walked_path.append([alice_position[0], alice_position[1]])
else:
    print("She did it! She went to the party.")

for i in walked_path:
    field[i[0]][i[1]] = '*'

[print(*r) for r in field]
