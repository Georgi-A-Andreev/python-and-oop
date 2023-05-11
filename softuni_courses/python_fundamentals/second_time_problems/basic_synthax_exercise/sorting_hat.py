while True:
    name = input()

    if name == 'Welcome!':
        break

    if name == 'Voldemort':
        print("You must not speak of that name!")
        exit()

    x = len(name)

    if x < 5:
        print(f"{name} goes to Gryffindor.")
    elif x == 5:
        print(f"{name} goes to Slytherin.")
    elif x == 6:
        print(f"{name} goes to Ravenclaw.")
    elif x > 6:
        print(f"{name} goes to Hufflepuff.")


print("Welcome to Hogwarts.")
