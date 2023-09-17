from collections import deque

expression = deque(input().split())
result = []
colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
special = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}
while expression:

    x = expression.popleft()
    y = expression.pop() if expression else ''

    for color in (x + y, y + x):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (x[:-1], y[:-1]):
            if el:
                expression.insert(len(expression) // 2, el)

for color in set(special.keys()).intersection(result):
    if not special[color].issubset(result):
        result.remove(color)
print(result)
