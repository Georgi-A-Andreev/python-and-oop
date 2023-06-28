courses = {}

while True:
    line = input()

    if line == 'end':
        break

    name, student = line.split(' : ')
    if name not in courses:
        courses[name] = []

    courses[name].append(student)

for k, v in courses.items():
    print(f'{k}: {len(v)}')
    [print(f'-- {el}') for el in v]
