health = 100
max_health = health
bitcoins = 0
counter = 0
alive = True
dungeon_rooms = input().split("|")

for room in dungeon_rooms:
    command, number = room.split()
    number = int(number)
    counter += 1

    if command == 'potion':
        if health + number > 100:
            print(f'You healed for {max_health - health} hp.')
            health = 100
        else:
            health += number
            print(f'You healed for {number} hp.')

        print(f'Current health: {health} hp.')

    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')

    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {counter}')
            alive = False
            break

if alive:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
