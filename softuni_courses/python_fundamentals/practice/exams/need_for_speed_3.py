n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split('|')
    cars[car] = [int(mileage), int(fuel)]

while True:
    command = input()
    if command == 'Stop':
        for k, v in cars.items():
            print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")
        break

    c = command.split(' : ')

    if c[0] == 'Drive':
        fuel = int(c[-1])
        distance = int(c[2])
        car = c[1]
        if fuel > cars[car][-1]:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car][0] >= 100_000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
    elif c[0] == 'Refuel':
        car = c[1]
        fuel = int(c[2])
        if cars[car][1] + fuel > 75:
            print(f"{car} refueled with {75 - cars[car][1]} liters")
            cars[car][1] = 75
        else:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif c[0] == 'Revert':
        car = c[1]
        km = int(c[2])
        if cars[car][0] - km <= 10_000:
            cars[car][0] = 10_000
            continue
        cars[car][0] -= km
        print(f"{car} mileage decreased by {km} kilometers")
