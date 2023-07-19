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

for i in range(cols - 1, -1, -1):
    if dp[rows - 1][i] != dp[rows - 1][i - 1]:
        path.appendleft(seq_1[i])

print(*path, sep=' ')
print(dp[rows - 1][cols - 1])
