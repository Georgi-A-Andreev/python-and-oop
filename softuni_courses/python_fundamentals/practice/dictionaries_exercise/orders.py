products = {}

while True:
    command = input()

    if command == 'buy':
        break

    name, price, quantity = command.split()
    if name not in products:
        products[name] = [0, 0]

    products[name][0] = float(price)
    products[name][1] += float(quantity)

[print(f'{k} -> {v[0] * v[1]:.2f}') for k, v in products.items()]
