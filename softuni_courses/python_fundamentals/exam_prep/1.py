stops = input()

while True:
    command = input()

    if command == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    command = command.split(':')

    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops):
            stops = stops[0:index] + string + stops[index:]

    elif command[0] == 'Remove Stop':
        start = int(command[1])
        end = int(command[2])
        if 0 <= start < len(stops) and 0 <= end < len(stops):
            stops = stops.replace(stops[start:end + 1], '')
    else:
        old_string = command[1]
        new_string = command[2]
        stops = stops.replace(old_string, new_string)
    print(stops)
