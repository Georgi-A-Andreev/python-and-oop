text = input()

while True:
    command = input()
    if command == 'Reveal':
        print(f"You have a new text message: {text}")
        break

    command = command.split(':|:')

    if command[0] == 'InsertSpace':
        text = text[:int(command[-1])] + ' ' + text[int(command[-1]):]

    elif command[0] == 'Reverse':
        if command[-1] not in text:
            print('error')
            continue
        else:
            text = text.replace(command[-1], '', 1)
            text = text + command[-1][::-1]

    elif command[0] == 'ChangeAll':
        text = text.replace(command[1], command[2])

    print(text)
