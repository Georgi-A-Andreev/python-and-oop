def find_fibonacci(n, memo):
    if n < 2:
        return n
    if n in memo:
        return memo[n]

    result = find_fibonacci(n - 1, memo) + find_fibonacci(n - 2, memo)
    memo[n] = result
    return result


n = int(input())
print(find_fibonacci(n, {}))
