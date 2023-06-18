chat = []

while True:
    line = input()

    if line == 'end':
        break

    command = line.split()
    action = command[0]

    if action == 'Chat':
        chat.append(command[-1])

    elif action == 'Delete':
        if command[-1] not in chat:
            continue

        chat.remove(command[-1])

    elif action == 'Edit':
        if command[1] not in chat:
            continue

        for el in range(len(chat)):
            if chat[el] == command[1]:
                chat[el] = command[-1]

    elif action == 'Pin':
        if command[-1] not in chat:
            continue

        for idx in range(len(chat)):
            if chat[idx] == command[-1]:
                chat.append(chat.pop(idx))

    elif action == 'Spam':
        for m in command[1:]:
            chat.append(m)

print(*chat, sep='\n')
