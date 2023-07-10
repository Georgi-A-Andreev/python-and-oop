energy = 100
coins = 100

events = input().split('|')

for i in events:
    event, value = i.split('-')
    value = int(value)

    current_energy = energy

    if event == 'rest':
        energy = min(100, energy + value)
        print(f"You gained {energy - current_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == 'order':
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue

        energy -= 30
        coins += value
        print(f"You earned {value} coins.")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            break
else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")

