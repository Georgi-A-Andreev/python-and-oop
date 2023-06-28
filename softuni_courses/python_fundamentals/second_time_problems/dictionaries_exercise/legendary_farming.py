materialss = {}
found = False

materialss['shards'] = 0
materialss['fragments'] = 0
materialss['motes'] = 0
while True:
    text = input().split()
    for i in range(0, len(text), 2):
        material = text[i + 1].lower()
        quantity = int(text[i])

        if material not in materialss:
            materialss[material] = 0
        materialss[material] += quantity

        if materialss['shards'] >= 250:
            print("Shadowmourne obtained!")
            materialss['shards'] -= 250
            found = True
            break
        elif materialss['fragments'] >= 250:
            print('Valanyr obtained!')
            materialss['fragments'] -= 250
            found = True
            break
        elif materialss['motes'] >= 250:
            print('Dragonwrath obtained!')
            materialss['motes'] -= 250
            found = True
            break
    if found:
        break
[print(f'{k}: {v}') for k, v in materialss.items()]