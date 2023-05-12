def func(n1, x1):
    if n1 == 'int':
        return int(x1) * 2
    elif n1 == 'real':
        return f'{float(x1) * 1.5:.2f}'
    elif n1 == 'string':
        return f'${x1}$'


n = input()
x = input()

print(func(n, x))
