from collections import deque

sequence = [int(x) for x in input().split()]

dp = [[1] * len(sequence), [None] * len(sequence)]

for idx in range(1, len(sequence)):
    for idx2 in range(idx - 1, -1, -1):
        if sequence[idx] > sequence[idx2]:
            if dp[0][idx2] + 1 >= dp[0][idx]:
                dp[1][idx] = idx2
                dp[0][idx] = dp[0][idx2] + 1

max_idx = 0

for idx, el in enumerate(dp[0]):
    if el > dp[0][max_idx]:
        max_idx = idx


path = deque()
idx = max_idx

while idx is not None:
    path.appendleft(sequence[idx])
    idx = dp[1][idx]

print(*path, sep=' ')
