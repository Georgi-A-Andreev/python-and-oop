from collections import deque

materials = deque([int(x) for x in input().split()])
magic_level = deque([int(x) for x in input().split()])

result = []
presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials and magic_level:
    mat = materials.pop()
    lvl = magic_level.popleft()

    if mat * lvl in presents.keys():
        result.append(presents[mat * lvl])
    elif mat * lvl < 0:
        materials.append(mat + lvl)
    elif mat * lvl > 0:
        materials.append(mat + 15)
    else:
        if mat == 0 and lvl != 0:
            magic_level.appendleft(lvl)
        elif mat != 0 and lvl == 0:
            materials.append(mat)

if ('Doll' in result and 'Train' in result) or ('Teddy bear' in result and 'Bicycle' in result):
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")
if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials][::-1])}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')

for i in sorted(set(result)):
    print(f'{i}: {result.count(i)}')
