n = int(input())
total_price = 0

for i in range(n):
    price = float(input())
    days = int(input())
    need = int(input())

    if not 0.01 <= price <= 100 or not 1 <= days <= 31 or not 1 <= need <= 2000:
        continue
    else:
        price_per_day = need * days * price
        total_price += price_per_day
        print(f"The price for the coffee is: ${price_per_day:.2f}")
else:
    print(f"Total: ${total_price:.2f}")
