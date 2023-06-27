result = {}

line = input().split()

for el in line:
    el = el.lower()

    if el not in result:
        result[el] = 0
    result[el] += 1

print(' '.join([str(el) for el in result if result[el] % 2 != 0]))
