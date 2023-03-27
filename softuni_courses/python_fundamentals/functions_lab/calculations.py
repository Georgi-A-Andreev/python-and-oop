def action(d, a1, b1):
    result = 0
    if d == 'multiply':
        result = a1 * b1
    elif d == 'divide':
        result = a1 // b1
    elif d == 'add':
        result = a1 + b1
    elif d == 'subtract':
        result = a1 - b1
    return result


deli = input()
a = int(input())
b = int(input())

print(action(deli, a, b))
