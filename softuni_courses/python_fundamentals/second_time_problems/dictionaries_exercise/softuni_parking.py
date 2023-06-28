users = {}
n = int(input())
for _ in range(n):
    command = input().split()
    name = command[1]
    if command[0] == 'register':
        if name not in users:
            users[name] = command[-1]
            print(f"{name} registered {command[-1]} successfully")
        else:
            print(f"ERROR: already registered with plate number {command[-1]}")
    else:
        if name in users:
            users.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

[print(f'{k} => {v}') for k, v in users.items()]
