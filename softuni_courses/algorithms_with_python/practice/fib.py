def fib(num):
    sum = 0
    a = 1
    b = 1

    for _ in range(num - 1):
        sum = a + b
        a, b = b, sum

    return sum


print(fib(int(input())))
