while True:
    name = input()

    if name == 'Welcome!':
        break

    x = len(name)

    if x < 5:
        print(f"{name} goes to Gryffindor.")
    elif x == 5:
        print(f"{name} goes to Slytherin.")
    elif x == 6:
        print(f"{name} goes to Ravenclaw.")
    elif x > 6:
        print()