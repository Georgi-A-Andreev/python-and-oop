text = input()

while True:
    command = input()
    if command == 'Done':
        break

    command = command.split()

    if command[0] == 'Change':
        char = command[1]
        replacement = command[2]

        while char in text:
            text = text.replace(char, replacement)

        print(text)

    elif command[0] == 'Includes':
        substring = command[1]
        if substring in text:
            print(True)
        else:
            print(False)

    elif command[0] == 'End':
        substring = command[1]
        if text.endswith(substring):
            print(True)
        else:
            print(False)

    elif command[0] == 'Uppercase':
        text = text.upper()

        print(text)

    elif command[0] == 'FindIndex':
        char = command[1]

        print(text.index(char))

    elif command[0] == 'Cut':
        startIndex = int(command[1])
        count = int(command[2])

        text = text[startIndex:startIndex + count]
        print(text)