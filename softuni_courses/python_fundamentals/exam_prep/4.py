concealed_message = input()

while True:
    command = input()

    if command == 'Reveal':
        break

    result = command.split(':|:')

    if result[0] == 'InsertSpace':
        index = int(result[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)
    elif result[0] == 'Reverse':
        substring = result[1]
        if substring not in concealed_message:
            print('error')
        else:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
            print(concealed_message)
    else:
        substring = result[1]
        replacement = result[2]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
print(f'You have a new text message: {concealed_message}')
