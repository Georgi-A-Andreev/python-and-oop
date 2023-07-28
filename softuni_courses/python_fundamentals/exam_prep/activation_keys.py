key = input()

while True:
    command = input()
    if command == 'Generate':
        print(f"Your activation key is: {key}")
        break

    if command.startswith('Contains'):
        substring = command.split('>>>')[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif command.startswith('Flip'):
        command, state, start, end = command.split('>>>')
        start = int(start)
        end = int(end)

        if state == 'Upper':
            key = key[:start] + key[start:end].upper() + key[end:]
        elif state == 'Lower':
            key = key[:start] + key[start:end].lower() + key[end:]
        print(key)

    elif command.startswith('Slice'):
        command, start, end = command.split('>>>')
        start = int(start)
        end = int(end)

        key = key[:start] + key[end:]

        print(key)