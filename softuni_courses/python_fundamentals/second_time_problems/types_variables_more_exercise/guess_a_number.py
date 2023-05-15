import random


def generate_random_number():

    return random.choice(range(1, 101))


def players_guess():
    choice = int(input('Please choose a number: '))

    return choice


def generate_clues(choice, number):
    if choice > number:
        result = 'Your number is too high'
    elif choice < number:
        result = 'Your number is too low'
    else:
        result = 'Congratulations, you guessed the number'

    print(result)


def main():
    random_number = generate_random_number()
    while True:
        current_choice = players_guess()
        generate_clues(current_choice, random_number)
        if current_choice == random_number:
            break


while True:
    main()
