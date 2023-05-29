gifts = input().split()

while True:
    command = input()

    if command == 'No Money':
        break

    if command.startswith('OutOfStock'):
        gift = command.split()[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = None

    elif command.startswith('Required'):
        gift = command.split()[1]
        index = int(command.split()[2])

        if 0 <= index < len(gifts):
            gifts[index] = gift

    else:
        gifts[-1] = command.split()[-1]

print(' '.join([i for i in gifts if i is not None]))
