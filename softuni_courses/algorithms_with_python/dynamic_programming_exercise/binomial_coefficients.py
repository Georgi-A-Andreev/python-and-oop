n = int(input())
k = int(input())


def find_binomial(n, k, memo):
    key = (n, k)
    if n == 0 or k == 0 or n == k:
        return 1
    if key in memo:
        return memo[key]

    result = find_binomial(n - 1, k, memo) + find_binomial(n - 1, k - 1, memo)
    if key not in memo:
        memo[key] = result

    return result


print(find_binomial(n, k, {}))
