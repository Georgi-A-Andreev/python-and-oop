def recursive_power(number, power):
    if power == 0:
        return 1
    result = 0
    result += recursive_power(number, power - 1) * number
    return result


print(recursive_power(2, 10))
print(recursive_power(10, 100))
