def choose_players_and_sign():
    player1 = input('Player one name: ')
    player2 = input('Player two name: ')
    player1_sign = input(f'{player1} would you like to play with "X" or "O"? ')
    if player1_sign == 'X':
        player2_sign = 'O'
    else:
        player2_sign = 'X'

    return [player1, player1_sign], [player2, player2_sign]


def print_field(first_player, first_time=True):
    if first_time:
        print('This is the numeration of the board:')
        for i in range(1, 10, 3):
            print(f'| {i} | {i + 1} | {i + 2} |')
        print(f'{first_player} starts first!')
    else:
        for r in field:
            print('| ', end='')
            print(' | '.join(str(i) for i in r), end='')
            print(' |')


def make_your_choice(player, sign):

    pick = int(input(f'{player} choose a free position [1-9]: '))
    if 0 <= pick < 10 and field[(pick - 1) // 3][(pick - 1) % 3] == ' ':
        field[(pick - 1) // 3][(pick - 1) % 3] = sign
    else:
        print('Invalid Position !!!')
        make_your_choice(player, sign)


def validation(matrix, current, current_sign):
    diagonal = all([matrix[i][i] == current_sign for i in range(len(matrix))])
    diagonal2 = all([matrix[i][len(matrix) - 1 - i] == current_sign for i in range(len(matrix))])
    vertical = all([matrix[i][0] == current_sign for i in range(len(matrix))])
    horizontal = any([len(set(matrix[r])) == 1 and current_sign in matrix[r] for r in range(len(matrix))])

    if any([diagonal, diagonal2, vertical, horizontal]):
        print(f'{current} won!')
        exit()


def start():
    current, other = choose_players_and_sign()
    print_field(current[0])
    while True:
        make_your_choice(current[0], current[1])
        print_field(current[0], False)
        validation(field, current[0], current[1])
        current, other = other, current


field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

start()
