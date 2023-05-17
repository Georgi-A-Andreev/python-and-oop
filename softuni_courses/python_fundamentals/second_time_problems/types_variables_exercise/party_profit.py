from math import floor

group_size = int(input())
days = int(input())

total = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2

    if i % 15 == 0:
        group_size += 5

    total += 50
    total -= 2 * group_size

    if i % 3 == 0:
        total -= group_size * 3

    if i % 5 == 0:
        total += group_size * 20
        if i % 3 == 0:
            total -= group_size * 2



print(f"{group_size} companions received {floor(total / group_size)} coins each.")
