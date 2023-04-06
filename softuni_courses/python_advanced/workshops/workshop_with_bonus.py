from collections import deque


def create_field(row, col):
    field = []
    for _ in range(row):
        field.append([0] * col)
    return field


def player_choice(player):
    return int(input(f'Player {current_player}, please choose a column:\n')) - 1


def print_field(matrix, player, choice):
    for i in range(len(matrix) - 1, -1, -1):
        if matrix[i][choice] == 0:
            matrix[i][choice] = player
            [print(i) for i in matrix]
            break
    return i, choice


def validation(field, player):
    for r in range(field):
        for c in field[r]:
            if c == player:
                lst = field[r][field.index(c):min(len(field[r]) - 1, field.index(c) + 4)]
                if field.index(c) <= len(field) - 4:
                    lst2 = [field[r + i][field.index(c)] for i in range(len(field) - 4)]
                if r >= 3 and matrix[r].index(c) <= len(matrix[r]) - 4:
                    lst3 = [field[r - i][field.index(c) + i] for i in range(len(field) - 4)]
                if r >= 3 and matrix[r].index(c) >= 3:
                    lst4 = [field[r - i][field.index(c) - i] for i in range(len(field) - 4)]
            for i in (lst, lst2, lst3, lst4):
                if len(i) == 4 and set(i) == 1:
                    return True


max_players = deque(range(1, int(input('How many players will play? : ')) + 1))
rows = int(input('How many rows? : '))
cols = int(input('How many cols? : '))
matrix = create_field(rows, cols)
current_player = max_players[0]
choice = player_choice(current_player)
print_field(matrix, current_player, choice)
if validation(matrix, current_player):
    print(f'The winner is player {current_player}')
    exit()

max_players.append(max_players.popleft())
