from collections import deque

textiles = deque(int(x) for x in input().split())
medicament = [int(x) for x in input().split()]

created_items = {}

items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}

while True:
    if not medicament and not textiles:
        print('Textiles and medicaments are both empty.')
        break
    elif not medicament:
        print("Medicaments are empty.")
        break
    elif not textiles:
        print("Textiles are empty.")
        break

    t = textiles.popleft()
    m = medicament.pop()

    if m + t in items:
        if items[m+t] not in created_items:
            created_items[items[m+t]] = 1
        else:
            created_items[items[m+t]] += 1

    elif m + t > 100:
        if items[100] not in created_items:
            created_items[items[100]] = 1
        else:
            created_items[items[100]] += 1
        medicament.append(medicament.pop() + (m + t) - 100)

    else:
        medicament.append(m + 10)


if created_items:
    for k, v in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
        print(f'{k} - {v}')

if medicament:
    medicament.reverse()
    print(f'Medicaments left: {", ".join(map(str, medicament))}')

if textiles:
    print(f'Textiles left: {", ".join(str(x) for x in textiles)}')
