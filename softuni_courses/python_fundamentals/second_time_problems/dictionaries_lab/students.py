result = {}

while True:
    line = input()

    if ':' not in line:
        break

    name, idd, course = line.split(':')

    if course not in result:
        result[course] = [f'{name} - {idd}']
    else:
        result[course].append(f'{name} - {idd}')

[print(el) for el in result[' '.join(line.split('_'))]]
