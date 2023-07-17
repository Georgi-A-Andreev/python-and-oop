first = list(input())
second = list(input())

dp = []

for _ in range(len(second) + 1):
    dp.append([0] * (len(first) + 1))

for row in range(1, len(second) + 1):
    for col in range(1, len(first) + 1):
        if first[col - 1] == second[row - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

print(dp[len(second)][len(first)])
