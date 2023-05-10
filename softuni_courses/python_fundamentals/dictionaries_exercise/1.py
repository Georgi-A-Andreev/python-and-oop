x = ''.join(input().split())
result = {}

for i in x:
    if i not in result:
        result[i] = 0

    result[i] += 1

for x, y in result.items():
    print(f"{x} -> {y}")
