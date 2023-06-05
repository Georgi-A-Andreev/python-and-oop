def fibonacci(n):
    a = 1
    b = 1
    result = 0

    for i in range(n - 1):
        result = a + b
        a, b = b, result

    if n == 1:
        return 1

    return result


n = int(input())
print(fibonacci(n))
