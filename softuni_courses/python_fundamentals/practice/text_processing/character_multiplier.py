strings = input().split()

result = 0
idx = 0

while True:
    if idx < len(strings[0]) and idx < len(strings[1]):
        result += ord(strings[0][idx]) * ord(strings[1][idx])

    if idx == len(strings[0]) == len(strings[1]):
        break
    if idx == len(strings[0]) - 1:
        for el in strings[1][idx + 1:]:
            result += ord(el)
        break
    if idx == len(strings[1]) - 1:
        for el in strings[0][idx + 1:]:
            result += ord(el)
        break
    idx += 1
print(result)