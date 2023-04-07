from functools import reduce


def operate(operator, *numbers):
    if operator == '+':
        return reduce(lambda x, y: x + y, numbers)

    elif operator == '-':
        return reduce(lambda x, y: x - y, numbers)

    elif operator == '*':
        return reduce(lambda x, y: x * y, numbers)

    else:
        if 0 not in numbers:
            return reduce(lambda x, y: x / y, numbers)


print(operate("*", 3, 4))
