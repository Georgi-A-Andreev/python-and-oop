from collections import deque

rows = int(input())
cols = int(input())

field = []
for _ in range(rows):
    field.append([int(x) for x in input().split()])

dp = []

for _ in range(rows):
    dp.append([0] * cols)

dp[0][0] = field[0][0]

for i in range(1, rows):
    dp[i][0] = dp[i - 1][0] + field[i][0]

for i in range(1, cols):
    dp[0][i] = dp[0][i - 1] + field[0][i]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row][col - 1], dp[row - 1][col]) + field[row][col]

path = deque()
row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    path.appendleft(f'[{row}, {col}]')
    if dp[row][col - 1] >= dp[row - 1][col]:
        col -= 1
    else:
        row -= 1

while row > 0:
    path.appendleft(f'[{row}, {col}]')
    row -= 1

while col > 0:
    path.appendleft(f'[{row}, {col}]')
    col -= 1

path.appendleft('[0, 0]')
print(*path, sep=' ')
