items = input().split('|')
budget = float(input())
budget_total = budget
bought_items_price = []

for i in items:
    item, price = i.split('->')
    price = float(price)
    if (item == 'Clothes' and price > 50) \
            or (item == 'Shoes' and price > 35) \
            or (item == 'Accessories' and price > 20.5):
        continue

    if budget - price < 0:
        continue

    budget -= price
    bought_items_price.append(price)

print(' '.join(f'{x * 1.4:.2f}' for x in bought_items_price))
print(f'Profit: {sum(bought_items_price) * 0.4:.2f}')

print('Hello, France!') if sum(bought_items_price) * 1.4 + budget >= 150 else print("Not enough money.")
