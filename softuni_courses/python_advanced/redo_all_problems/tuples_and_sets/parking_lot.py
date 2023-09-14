commands = int(input())
parking = set()
for _ in range(commands):
    direction, plate = input().split(', ')

    if direction == 'IN':
        parking.add(plate)

    else:
        if plate in parking:
            parking.remove(plate)

if parking:
    print(*parking, sep='\n')
else:
    print('Parking Lot is Empty')
