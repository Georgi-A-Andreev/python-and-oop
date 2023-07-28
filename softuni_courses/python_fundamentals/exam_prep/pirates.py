targets = {}

while True:
    text = input()
    if text == 'Sail':
        break

    text = text.split('||')
    if text[0] not in targets:
        targets[text[0]] = [0] * 2
    targets[text[0]][0] += int(text[1])
    targets[text[0]][1] += int(text[2])

while True:
    command = input()
    if command == 'End':
        break

    command = command.split('=>')

    if command[0] == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        targets[town][0] -= people
        targets[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targets[town][0] <= 0 or targets[town][1] <= 0:
            targets.pop(town)
            print(f"{town} has been wiped off the map!")

    elif command[0] == 'Prosper':
        town = command[1]
        gold = int(command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        targets[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {targets[town][1]} gold.")

if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for k, v in targets.items():
        print(f"{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

