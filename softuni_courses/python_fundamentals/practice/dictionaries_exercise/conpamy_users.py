company = {}

while True:
    command = input()
    if command == 'End':
        break
    name, id = command.split(' -> ')

    if name not in company:
        company[name] = []
    if id not in company[name]:
        company[name].append(id)

for k, v in company.items():
    print(k)
    [print(f'-- {el}') for el in v]
