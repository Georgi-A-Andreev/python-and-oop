first = input()
second = input()

cols = len(first) + 1
rows = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for i in range(1, cols):
    dp[0][i] = i

for i in range(1, rows):
    dp[i][0] = i

for row in range(1, rows):
    for col in range(1, cols):
        if first[col - 1] == second[row - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

print(f'Deletions and Insertions: {dp[rows - 1][cols - 1]}')
