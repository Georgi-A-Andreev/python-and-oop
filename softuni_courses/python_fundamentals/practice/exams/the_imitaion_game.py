encrypted_text = input()

command = input()

while command != 'Decode':
    command = command.split('|')
    action = command[0]

    if action == 'Move':
        count = int(command[1])
        encrypted_text = encrypted_text[count:] + encrypted_text[:count]
    elif action == 'Insert':
        idx = int(command[1])
        value = command[-1]
        encrypted_text = encrypted_text[:idx] + value + encrypted_text[idx:]
    elif action == 'ChangeAll':
        substring = command[1]
        replacement = command[2]

        while substring in encrypted_text:
            encrypted_text = encrypted_text.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {encrypted_text}')