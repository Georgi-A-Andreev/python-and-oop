stops = input()

while True:
    command = input()
    if command == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    command, first, second = command.split(':')

    if command == 'Add Stop':
        if 0 <= int(first) < len(stops):
            stops = stops[:int(first)] + second + stops[int(first):]

    elif command == 'Remove Stop':
        first = int(first)
        second = int(second)
        if 0 <= first < len(stops) and 0 <= second < len(stops):
            stops = stops.replace(stops[first:second + 1], '')

    elif command == 'Switch':

        stops = stops.replace(first, second)

    print(stops)
