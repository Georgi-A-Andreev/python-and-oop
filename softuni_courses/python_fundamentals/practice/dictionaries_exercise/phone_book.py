result = {}
while True:
    line = input()

    if line.isdigit():
        break

    contact, number = line.split('-')

    result[contact] = number

for n in range(int(line)):
    name = input()
    if name not in result:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {result[name]}')
