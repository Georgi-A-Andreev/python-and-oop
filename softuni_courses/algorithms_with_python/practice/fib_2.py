n = int(input())


def find_fib(n, memo):
    if n in memo:
        return memo[n]
    if n < 2:
        return n

    result = find_fib(n - 1, memo) + find_fib(n - 2, memo)
    memo[n] = result

    return result


print(find_fib(n, {}))
