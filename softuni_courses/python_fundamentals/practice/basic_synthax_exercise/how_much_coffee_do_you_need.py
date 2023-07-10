total_coffees = 0

while True:
    command = input()

    if command == 'END':
        break

    if command.lower() not in ['coding', 'dog', 'cat', 'movie']:
        continue

    if command.upper() == command:
        total_coffees += 2
    else:
        total_coffees += 1

if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)
