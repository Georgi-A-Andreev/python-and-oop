pirate_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
max_health = int(input())
is_true = True
while is_true:
    command = input()

    if command == 'Retire':
        break

    command_list = command.split()

    if command_list[0] == 'Fire':
        if 0 <= int(command_list[1]) < len(warship_status):
            warship_status[int(command_list[1])] -= int(command_list[-1])
            if warship_status[int(command_list[1])] <= 0:
                is_true = False
                print(f'You won! The enemy ship has sunken.')

    elif command_list[0] == 'Defend':
        if (0 <= int(command_list[1]) < len(pirate_status)) and \
                (0 <= int(command_list[2]) < len(pirate_status)):
            for i in range(int(command_list[1]), int(command_list[2]) + 1):
                pirate_status[i] -= int(command_list[-1])
                if pirate_status[i] <= 0:
                    is_true = False
                    print('You lost! The pirate ship has sunken.')
                    break

    elif command_list[0] == 'Repair':
        if 0 <= int(command_list[1]) < len(pirate_status):
            pirate_status[int(command_list[1])] = \
                min(pirate_status[int(command_list[1])] + int(command_list[-1]), max_health)
    elif command_list[0] == 'Status':
        status = [x for x in pirate_status if x < max_health * 0.2]
        print(f'{len(status)} sections need repair.')

if is_true:
    print(f'Pirate ship status: {sum(pirate_status)}')
    print(f'Warship status: {sum(warship_status)}')
