from functools import reduce
from math import floor

expression = input().split()
container = []

for el in expression:
    result = 0
    if el.isdigit() or len(el) == 2:
        container.append(int(el))
        continue

    elif el == '+':
        result = reduce(lambda x, y: x + y, container)

    elif el == '*':
        result = reduce(lambda x, y: x * y, container)

    elif el == '-':
        result = reduce(lambda x, y: x - y, container)

    elif el == '/':
        result = floor(reduce(lambda x, y: x // y, container))

    container = [result]
print(container[0])