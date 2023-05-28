tax = 0
total_amount_no_tax = 0

while True:
    price = input()

    if price == 'special' or price == 'regular':
        break

    price = float(price)
    if price <= 0:
        print('Invalid price!')
        continue

    tax += 0.2 * price
    total_amount_no_tax += price
total_price_with_tax = total_amount_no_tax + tax
if price == 'special':
    total_price_with_tax *= 0.9

if total_amount_no_tax == 0:
    print('Invalid order!')
    exit()

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_amount_no_tax:.2f}$")
print(f"Taxes: {tax:.2f}$")
print("-----------")
print(f"Total price: {total_price_with_tax:.2f}$")
