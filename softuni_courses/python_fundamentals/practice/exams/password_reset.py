text = input()

while True:
    command = input()

    if command == 'Done':
        print(f"Your password is: {text}")
        break

    command = command.split()

    if command[0] == 'TakeOdd':
        new_password = ''
        for i in range(1, len(text), 2):
            new_password += text[i]
        text = new_password
        print(text)

    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])

        text = text[:index] + text[index + length:]
        print(text)

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]

        if substring in text:
            while substring in text:
                text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")