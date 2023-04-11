def shop_from_grocery_list(*args):
    budged, lst, *items = args
    bought_items = []

    for p, price in items:
        if p in lst and p not in bought_items:
            if price <= budged:
                bought_items.append(p)
                budged -= price
                lst.remove(p)
            else:
                break

    if lst:
        return f'You did not buy all the products. Missing products: {", ".join(lst)}.'
    return f'Shopping is successful. Remaining budget: {budged:.2f}.'


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
