prices = {
    'coffee': 1.50,
    'water': 1.00,
    'coke': 1.40,
    'snacks': 2.00,
}


def calculate_order(product, quantity):
    return f'{prices[product] * quantity:.2f}'


product_name = input()
product_quantity = int(input())

print(calculate_order(product_name, product_quantity))
