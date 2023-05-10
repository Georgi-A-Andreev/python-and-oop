import re
total_price = 0
bought_items = []
pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'


while True:
    text = input()
    if text == 'Purchase':
        break
    result = re.match(pattern, text)
    if result:
        item, price, quant = result.groups()
        bought_items.append(item)
        total_price += float(price) * int(quant)

print('Bought furniture:')
for i in bought_items:
    print(i)
print(f'Total money spend: {total_price:.2f}')
