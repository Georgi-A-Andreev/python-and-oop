result = {}
while True:
    x = input()

    if x == "statistics":
        break

    product, quantity = x.split(": ")
    quantity = int(quantity)
    if product not in result:
        result[product] = quantity
    else:
        result[product] += quantity

print("Products in stock:")
for i, j in result.items():
    print(f"- {i}: {j}")
print(f'Total Products: {len(result)}')
print(f'Total Quantity: {sum(result.values())}')
