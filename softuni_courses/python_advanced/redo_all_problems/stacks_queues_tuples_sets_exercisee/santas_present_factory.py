from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

presents_crafter = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while materials and magic_level:
    mat = materials.pop()
    if mat == 0:
        continue
    magic = magic_level.popleft()
    if magic == 0:
        materials.append(mat)
        continue
    total = mat * magic

    if total in presents:
        presents_crafter[presents[total]] += 1
        continue

    if total < 0:
        materials.append(mat + magic)

    if total > 0:
        materials.append(mat + 15)

if (presents_crafter['Doll'] and presents_crafter['Wooden train']) \
        or(presents_crafter['Teddy bear'] and presents_crafter['Bicycle']):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for k, v in sorted(presents_crafter.items()):
    if v > 0:
        print(f"{k}: {v}")
