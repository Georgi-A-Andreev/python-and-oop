def factorial_devision(a, b):
    first_factorial = 1
    second_factorial = 1

    for i in range(1, a + 1):
        first_factorial *= i

    for i in range(1, b + 1):
        second_factorial *= i

    return f'{first_factorial / second_factorial:.2f}'


a = int(input())
b = int(input())

print(factorial_devision(a, b))