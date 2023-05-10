result = {}
while True:
    product = input()
    if product == "stop":
        break

    resource = int(input())

    if product not in result:
        result[product] = 0

    result[product] += resource

for i, y in result.items():
    print(f"{i} -> {y}")