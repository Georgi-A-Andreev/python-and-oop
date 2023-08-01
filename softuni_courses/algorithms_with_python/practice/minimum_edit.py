replace = int(input())
insert = int(input())
delete = int(input())

s1 = input()
s2 = input()

rows = len(s1) + 1
cols = len(s2) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for i in range(1, rows):
    dp[i][0] = dp[i - 1][0] + delete

for i in range(1, cols):
    dp[0][i] = dp[0][i - 1] + insert

for row in range(1, rows):
    for col in range(1, cols):
        if s2[col - 1] == s1[row - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1] + insert, dp[row - 1][col] + delete, dp[row - 1][col - 1] + replace)

print(f'Minimum edit distance: {dp[rows - 1][cols - 1]}')