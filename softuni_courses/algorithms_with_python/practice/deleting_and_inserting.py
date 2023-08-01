first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for i in range(rows):
    dp[i][0] = i

for i in range(cols):
    dp[0][i] = i

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + 1

print(f'Deletions and Insertions: {dp[rows - 1][cols - 1]} ')