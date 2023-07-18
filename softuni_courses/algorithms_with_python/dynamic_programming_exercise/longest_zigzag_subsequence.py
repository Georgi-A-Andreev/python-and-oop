from collections import deque

sequence = [int(x) for x in input().split()]

prev = [None] * len(sequence)
max_seq = [1] * len(sequence)
dp = []
[dp.append([0] * len(sequence)) for _ in range(2)]
parent = []
[parent.append([None] * len(sequence)) for _ in range(2)]
dp[0][0] = dp[1][0] = 1
best_size = 0
best_rol = 0
best_col = 0
for idx in range(1, len(sequence)):
    current_number = sequence[idx]

    for prev in range(idx - 1, -1, -1):
        prev_number = sequence[prev]

        if current_number > prev_number and dp[1][prev] + 1 >= dp[0][idx]:
            dp[0][idx] = dp[1][prev] + 1
            parent[0][idx] = prev

        if prev_number > current_number and dp[0][prev] >= dp[1][idx]:
            dp[1][idx] = dp[0][prev] + 1
            parent[1][idx] = prev

    if dp[0][idx] > best_size:
        best_size = dp[0][idx]
        best_col = idx
        best_rol = 0
    if dp[1][idx] > best_size:
        best_size = dp[1][idx]
        best_col = idx
        best_rol = 1

result = deque()
while best_col is not None:
    result.appendleft(sequence[best_col])
    best_col = parent[best_rol][best_col]
    best_rol = 1 if best_rol == 0 else 0

print(*result, sep=' ')
