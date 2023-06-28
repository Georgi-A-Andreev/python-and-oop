students = {}

n = int(input())

for _ in range(n):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
    students[student].append(grade)

[print(f'{k} -> {sum(v) / len(v):.2f}') for k, v in students.items() if sum(v) / len(v) >= 4.5]
