products = {}

while True:
    command = input()

    if command == 'statistics':
        break

    key, value = command.split(': ')
    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)

print('Products in stock:')
[print(f'- {k}: {v}') for k,v in products.items()]
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')
