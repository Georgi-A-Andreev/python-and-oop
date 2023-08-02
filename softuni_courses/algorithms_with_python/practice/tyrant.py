def minimum_sum_subsequence(sequence):
    n = len(sequence)
    if n <= 4:
        return min(sequence)

    dp = [0] * n
    dp[0] = sequence[0]
    dp[1] = sequence[1]
    dp[2] = sequence[2]
    dp[3] = sequence[3]

    for i in range(4, n):
        dp[i] = sequence[i] + min(dp[i - 4], dp[i - 3], dp[i - 2], dp[i - 1])

    return min(dp[-4:])


input_sequence = [int(x) for x in input().split()]
result = minimum_sum_subsequence(input_sequence)
print(result)

