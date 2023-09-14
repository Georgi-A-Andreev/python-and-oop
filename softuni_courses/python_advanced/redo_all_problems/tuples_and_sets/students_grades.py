count = int(input())
info = {}

for _ in range(count):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in info:
        info[name] = []

    info[name].append(grade)

for name, grades in info.items():
    print(f"{name} -> {' '.join(str(f'{x:.2f}') for x in grades)} (avg: {sum(grades) / len(grades):.2f})")
