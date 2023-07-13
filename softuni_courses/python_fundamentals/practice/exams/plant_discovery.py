n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    plants[plant] = [int(rarity)]

while True:
    command = input()
    if command == 'Exhibition':
        break

    command = command.split(': ')
    plant = command[1].split(' - ')[0]
    if plant not in plants:
        print('error')
        continue

    if command[0] == 'Rate':
        rating = int(command[1].split(' - ')[-1])
        plants[plant].append(rating)

    elif command[0] == 'Update':
        new_rarity = int(command[1].split(' - ')[-1])
        plants[plant][0] = new_rarity

    elif command[0] == 'Reset':
        plants[plant] = [plants[plant][0]]

print(f'Plants for the exhibition:')
for k, v in plants.items():
    if len(v) > 1:
        ratings = sum(v[1:]) / len(v[1:])
        print(f'- {k}; Rarity: {v[0]}; Rating: {ratings:.2f}')
    else:
        print(f'- {k}; Rarity: {v[0]}; Rating: 0.00')