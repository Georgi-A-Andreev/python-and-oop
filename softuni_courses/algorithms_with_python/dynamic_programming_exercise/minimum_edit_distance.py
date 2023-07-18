cost = int(input())
insert = int(input())
delete = int(input())
s1 = input()
s2 = input()

rows = len(s1) + 1
cols = len(s2) + 1

dp = []
for _ in range(rows):
    dp.append([0] * cols)

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + insert

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + delete

for row in range(1, rows):
    for col in range(1, cols):
        if s1[row - 1] == s2[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1] + insert, dp[row - 1][col] + delete, dp[row - 1][col - 1] + cost)

print(f'Minimum edit distance: {dp[rows - 1][cols - 1]}')
