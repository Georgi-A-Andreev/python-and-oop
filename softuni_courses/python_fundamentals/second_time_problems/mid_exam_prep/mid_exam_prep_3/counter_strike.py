energy = int(input())
counter = 0

while True:
    distance = input()

    if distance == 'End of battle':
        print(f"Won battles: {counter}. Energy left: {energy}")
        break

    distance = int(distance)
    if energy - distance < 0:
        print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
        break

    counter += 1
    energy -= distance

    if counter % 3 == 0:
        energy += counter