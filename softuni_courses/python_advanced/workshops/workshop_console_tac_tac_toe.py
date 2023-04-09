def choose_players_and_sign():
    player1 = input('Player one name: ')
    player2 = input('Player two name: ')
    player1_sign = input(f'{player1} would you like to play with "X" or "O"? ')
    if player1_sign == 'X':
        player2_sign = 'O'
    else:
        player2_sign = 'X'

    return [player1, player1_sign], [player2, player2_sign]


def print_field(first_time=True):
    if first_time:
        for i in range(1, 10, 3):
            print(f'| {i} | {i + 1} | {i + 2} |')
        first_time = True
    else:
        for r in field:
            print('| ', end='')
            print(' | '.join(str(i) for i in r), end='')
            print(' |')


field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print_field()

field[1][1] = 'X'
print_field(False)

