animals = {}
areas = {}

while True:
    command = input()
    if command == 'EndDay':
        break

    command = command.split(': ')

    if command[0] == 'Add':
        name, needed_food, area = command[1].split('-')
        needed_food = int(needed_food)
        if name not in animals:
            animals[name] = 0
        animals[name] += needed_food

        if area not in areas:
            areas[area] = []
        if name not in areas[area]:
            areas[area].append(name)

    elif command[0] == 'Feed':
        name, food = command[1].split('-')
        food = int(food)
        if name not in animals:
            continue

        animals[name] -= food

        if animals[name] <= 0:
            print(f'{name} was successfully fed')
            animals.pop(name)
            for k, v in areas.items():
                for an in v:
                    if an == name:
                        areas[k].remove(an)

print('Animals:')
for k, v in animals.items():
    print(f' {k} -> {v}g')

print('Areas with hungry animals:')
for k, v in areas.items():
    if v:
        print(f' {k}: {len(v)}')
