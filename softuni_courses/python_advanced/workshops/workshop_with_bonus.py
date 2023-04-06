from collections import deque


def create_field(row, col):
    field = []
    for _ in range(row):
        field.append([0] * col)
    return field


def player_choice(player):
    while True:
        current_pick = int(input(f'Player {player}, please choose a column: ')) - 1
        try:
            if not 0 <= current_pick <= cols:
                raise IndexError
        except IndexError:
            print('Invalid position, try again!')
        else:
            return current_pick


def print_field(matrix, player, choice):
    for i in range(len(matrix) - 1, -1, -1):
        if matrix[i][choice] == 0:
            matrix[i][choice] = player
            [print(i) for i in matrix]
            break


def validation(field, player, combinations_to_win):
    lst, lst2, lst3, lst4 = [], [], [], []
    for r in range(len(field)):
        for c in field[r]:
            if c == player:
                lst = field[r][field[r].index(c):min(len(field[r]), field[r].index(c) + combinations_to_win)]
                if r <= len(field) - combinations_to_win:
                    lst2 = [field[r + i][field[r].index(c)] for i in range(combinations_to_win)]
                if r >= combinations_to_win - 1 and matrix[r].index(c) <= len(matrix[r]) - combinations_to_win:
                    lst3 = [field[r - i][field[r].index(c) + i] for i in range(combinations_to_win)]
                if r >= combinations_to_win - 1 and matrix[r].index(c) >= combinations_to_win - 1:
                    lst4 = [field[r - i][field[r].index(c) - i] for i in range(combinations_to_win)]
                for i in (lst, lst2, lst3, lst4):
                    if len(i) == combinations_to_win and len(set(i)) == 1:
                        return 'winner'


max_players = deque(range(1, int(input('How many players will play? : ')) + 1))
rows = int(input('How many rows? : '))
cols = int(input('How many cols? : '))
combinations = int(input('How many positions in a row to win? : '))
matrix = create_field(rows, cols)

while True:
    current_player = max_players[0]
    choice = player_choice(current_player)
    print_field(matrix, current_player, choice)
    if validation(matrix, current_player, combinations) == 'winner':
        print(f'The winner is player {current_player}')
        break
    max_players.append(max_players.popleft())
