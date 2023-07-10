result = {}

while True:
    resource = input()

    if resource == 'stop':
        break

    quantity = int(input())

    if resource not in result:
        result[resource] = 0

    result[resource] += quantity

[print(f'{k} -> {v}') for k, v in result.items()]
