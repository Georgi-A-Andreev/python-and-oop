def calculate(op, num1, num2):
    if op == 'multiply':
        result = num2 * num2

    elif op == 'divide':
        result = num1 // num2

    elif op == 'add':
        result = num2 + num1

    else:
        result = num1 - num2

    return result


operator = input()
first = int(input())
second = int(input())

print(calculate(operator, first, second))