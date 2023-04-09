def choose_players_and_sign():
    player1 = input('Player one name: ')
    player2 = input('Player two name: ')
    player1_sign = input(f'{player1} would you like to play with "X" or "O"? ')
    if player1_sign == 'X':
        player2_sign = 'O'
    else:
        player2_sign = 'X'

    return (player1, player1_sign), (player2, player2_sign)


