n = int(input())

total = 0
for i in range(n):
    water = int(input())
    if water + total > 255:
        print('Insufficient capacity!')
        continue

    total += water

print(total)
