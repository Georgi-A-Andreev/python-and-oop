n = int(input())
pieces = {}
for _ in range(n):
    piece, composer, key = input().split('|')
    pieces[piece] = [composer, key]

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split('|')
    action = command[0]

    if action == 'Add':
        if command[1] in pieces:
            print(f'{command[1]} is already in the collection!')
        else:
            pieces[command[1]] = [command[2], command[3]]
            print(f"{command[1]} by {command[2]} in {command[-1]} added to the collection!")
    elif action == 'Remove':
        if command[1] in pieces:
            pieces.pop(command[1])
            print(f'Successfully removed {command[1]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')
    elif action == 'ChangeKey':
        if command[1] in pieces:
            pieces[command[1]][1] = command[2]
            print(f'Changed the key of {command[1]} to {command[2]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')

for k, v in pieces.items():
    print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")
