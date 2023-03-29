result = {}

for i in input():
    if i not in result:
        result[i] = 0

    result[i] += 1

[print(f'{i}: {j} time/s') for i, j in sorted(result.items())]
