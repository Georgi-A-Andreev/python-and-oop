number = int(input())


def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)


print(factorial(number))