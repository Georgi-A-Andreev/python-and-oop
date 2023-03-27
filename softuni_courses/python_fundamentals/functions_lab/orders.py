def my_func(p, q):
    result = 0
    if p == 'coffee':
        result = q * 1.5
    elif p == 'water':
        result = q
    elif p == 'coke':
        result = q * 1.4
    elif p == 'snacks':
        result = q * 2
    return result


product = input()
quantity = int(input())

print(f'{my_func(product, quantity):.2f}')
