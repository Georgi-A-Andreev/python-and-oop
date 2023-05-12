initial_list = input().split("!")


while True:
    commands = input()

    if commands == 'Go Shopping!':
        break

    commands_list = commands.split()

    if commands_list[0] == 'Urgent':
        if commands_list[1] not in initial_list:
            initial_list.insert(0, commands_list[1])
    elif commands_list[0] == 'Unnecessary':
        if commands_list[1] in initial_list:
            initial_list.remove(commands_list[1])
    elif commands_list[0] == 'Correct':
        counter = 0
        for i in initial_list:
            counter += 1
            if i == commands_list[1]:
                initial_list[counter - 1] = commands_list[2]
    elif commands_list[0] == 'Rearrange':
        if commands_list[1] in initial_list:
            initial_list.remove(commands_list[1])
            initial_list.append(commands_list[1])

print(", ".join(initial_list))
