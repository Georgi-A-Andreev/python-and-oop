text = input()
result = {}
for char in text:
    if char == ' ':
        continue

    if char not in result:
        result[char] = 0

    result[char] += 1

[print(f'{k} -> {v}') for k, v in result.items()]
