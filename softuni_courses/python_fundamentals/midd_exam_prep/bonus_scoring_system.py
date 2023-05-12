from math import ceil

students = int(input())
total_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
winner_attendance = 0

for i in range(students):
    attendance = int(input())

    if total_lectures == 0:
        total_bonus = 0
    else:
        total_bonus = (attendance / total_lectures) * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        winner_attendance = attendance

print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {winner_attendance} lectures.')

