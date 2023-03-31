parking_lot = set()

for i in range(int(input())):
    action, number = input().split(", ")
    if action == 'IN':
        parking_lot.add(number)
    else:
        parking_lot.discard(number)

print(*parking_lot, sep='\n') if parking_lot else print('Parking Lot is Empty')
