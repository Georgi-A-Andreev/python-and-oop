from collections import deque

seq_1 = [int(x) for x in input().split()]
seq_2 = [int(x) for x in input().split()]

rows = len(seq_1) + 1
cols = len(seq_2) + 1

dp = []

[dp.append([0] * cols) for _ in range(rows)]
path = deque()

for idx in range(1, rows):
    for idx2 in range(1, cols):
        if seq_1[idx - 1] == seq_2[idx2 - 1]:
            dp[idx][idx2] = dp[idx - 1][idx2 - 1] + 1

        else:
            dp[idx][idx2] = max(dp[idx - 1][idx2], dp[idx][idx2 - 1])

row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    if seq_1[row - 1] == seq_2[col - 1]:
        path.appendleft(seq_1[row - 1])
        row -= 1
        col -= 1

    elif dp[row][col - 1] < dp[row - 1][col]:
        row -= 1
    else:
        col -= 1


print(*path, sep=' ')
print(dp[rows - 1][cols - 1])
