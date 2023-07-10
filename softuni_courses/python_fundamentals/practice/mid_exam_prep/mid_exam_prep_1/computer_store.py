total_price_no_tax = 0
is_special = False
while True:
    price = input()

    if price == 'special':
        is_special = True
        break

    if price == 'regular':
        break

    price = float(price)

    if price < 0:
        print('Invalid price!')
        continue

    total_price_no_tax += price

if total_price_no_tax == 0:
    print('Invalid order!')
else:
    print(f'''Congratulations you've just bought a new computer!
Price without taxes: {total_price_no_tax:.2f}$
Taxes: {total_price_no_tax * 0.2:.2f}$
-----------
Total price: {total_price_no_tax * 1.2 if not is_special else (total_price_no_tax * 1.2) * 0.9:.2f}$
''')
