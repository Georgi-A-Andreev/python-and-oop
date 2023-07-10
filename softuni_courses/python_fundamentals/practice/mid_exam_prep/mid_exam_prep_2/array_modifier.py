array = [int(i) for i in input().split()]

while True:
    command = input()

    if command == 'end':
        break

    command = command.split()
    if command[0] == 'swap':
        idx1 = int(command[1])
        idx2 = int(command[2])
        array[idx1], array[idx2] = array[idx2], array[idx1]

    elif command[0] == 'multiply':
        idx1 = int(command[1])
        idx2 = int(command[2])
        array[idx1] *= array[idx2]

    else:
        for el in range(len(array)):
            array[el] -= 1

print(', '.join(str(x) for x in array))
