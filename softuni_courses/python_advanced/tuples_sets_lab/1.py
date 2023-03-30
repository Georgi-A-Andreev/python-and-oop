result = {}

for i in input().split():
    if i not in result:
        result[i] = 0

    result[i] += 1

for key, value in result.items():
    print(f"{float(key):.1f} - {value} times")
