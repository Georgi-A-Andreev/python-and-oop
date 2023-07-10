targets = [int(x) for x in input().split()]

while True:
    command = input()

    if command == 'End':
        print(f'{"|".join(map(str, targets))}')
        break

    command, idx, action = command.split()
    idx = int(idx)
    action = int(action)

    if command == 'Shoot':
        if 0 <= idx < len(targets):
            targets[idx] -= action
            if targets[idx] <= 0:
                targets.pop(idx)

    elif command == 'Add':
        if 0 <= idx < len(targets):
            targets.insert(idx, action)
        else:
            print("Invalid placement!")

    elif command == 'Strike':
        if action <= idx < len(targets) - action:
            for i in range(idx + action, idx - action - 1, -1):
                targets.pop(i)
        else:
            print('Strike missed!')

