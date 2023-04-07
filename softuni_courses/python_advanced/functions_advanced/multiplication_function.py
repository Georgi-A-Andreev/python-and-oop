from functools import reduce


def multiply(*numbers):

    total_sum = reduce(lambda x, y: x * y, numbers)
    return total_sum


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
