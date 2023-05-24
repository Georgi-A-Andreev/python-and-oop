size = int(input())
days = int(input())

total_coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        size -= 2

    if i % 15 == 0:
        size += 5

    total_coins += 50
    total_coins -= 2 * size

    if i % 3 == 0:
        total_coins -= 3 * size

    if i % 5 == 0:
        total_coins += 20 * size

    if i % 3 == 0 and i % 5 == 0:
        total_coins -= 2 * size


print(f'{size} companions received {int(total_coins / size)} coins each.')
