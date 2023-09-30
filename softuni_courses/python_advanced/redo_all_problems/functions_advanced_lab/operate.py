from functools import reduce


def operate(operator, *nums):
    if operator == '+':
        return reduce(lambda x, y: x + y, nums)
    if operator == '-':
        return reduce(lambda x, y: x - y, nums)
    if operator == '*':
        return reduce(lambda x, y: x * y, nums)
    if operator == '/':
        return reduce(lambda x, y: x / y, nums)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
