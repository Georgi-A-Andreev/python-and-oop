first = input()
second = input()

dp = []
[dp.append([0] * (len(second) + 1)) for _ in range(len(first) + 1)]

for row in range(1, len(first) + 1):
    for col in range(1, len(second) + 1):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[len(first)][len(second)])
