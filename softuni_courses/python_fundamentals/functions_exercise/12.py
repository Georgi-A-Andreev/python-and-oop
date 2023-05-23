def func(a1):
    fact1 = 1
    for i in range(1, a1 + 1):
        fact1 *= i
    return fact1


a = int(input())
b = int(input())

x = func(a) / func(b)

print(f'{x:.2f}')
