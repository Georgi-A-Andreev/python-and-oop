n = int(input())
current = 1
result = []

while True:
    if n <= 0:
        break

    formula = min(n, 2 * (current ** 2))

    n -= formula
    result.append(formula)
    current += 1

print(result)
