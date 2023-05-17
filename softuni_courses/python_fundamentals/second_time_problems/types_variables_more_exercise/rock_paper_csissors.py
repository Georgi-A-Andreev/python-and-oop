import random


def welcome():
    player_choice = input('What would you choose'
                          ' [r]ock, [p]aper, [c]sissors :')

    computer_choice = random.choice("rpc")
    print(f'Computer chooses - {computer_choice}')

    return player_choice, computer_choice


def validate_winner(player_choice, computer_choice):
    result = ''
    if player_choice == computer_choice:
        return 'DRAW'

    if player_choice == 'r':
        if computer_choice == 'p':
            result = 'Computer wins !!!'
        elif computer_choice == 'c':
            result = 'You win !!!'

    elif player_choice == 'p':
        if computer_choice == 'c':
            result = 'Computer wins !!!'
        elif computer_choice == 'r':
            result = 'You win !!!'

    elif player_choice == 'c':
        if computer_choice == 'r':
            result = 'Computer wins !!!'
        elif computer_choice == 'p':
            result = 'You win !!!'

    return result


def repeat():
    answer = input('If you don"t want to play again press [n] , otherwise press any button to play again')

    return answer


def main():
    while True:
        player, computer = welcome()
        print(validate_winner(player, computer))
        if repeat() == 'n':
            break


main()
