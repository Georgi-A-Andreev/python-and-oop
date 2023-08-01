def longest_zigzag_subsequence(sequence):
    n = len(sequence)
    if n <= 2:
        return sequence

    up_dp = [1] * n
    down_dp = [1] * n
    up_prev = [-1] * n
    down_prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j] and up_dp[i] < down_dp[j] + 1:
                up_dp[i] = down_dp[j] + 1
                up_prev[i] = j
            elif sequence[i] < sequence[j] and down_dp[i] < up_dp[j] + 1:
                down_dp[i] = up_dp[j] + 1
                down_prev[i] = j

    end_index = n - 1 if max(up_dp[-1], down_dp[-1]) > max(up_dp[-2], down_dp[-2]) else n - 2

    zigzag_subsequence = [sequence[end_index]]
    direction = 1 if up_dp[end_index] > down_dp[end_index] else -1

    while end_index != -1:
        if direction == 1:
            end_index = up_prev[end_index]
        else:
            end_index = down_prev[end_index]

        if end_index != -1:
            zigzag_subsequence.append(sequence[end_index])
            direction *= -1

    return zigzag_subsequence[::-1]


sequence = [int(x) for x in input().split()]
result = longest_zigzag_subsequence(sequence)
print(' '.join(str(x) for x in result))
