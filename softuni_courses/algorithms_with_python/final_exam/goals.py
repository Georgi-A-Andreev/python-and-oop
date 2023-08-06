from collections import deque

sequence = [int(x) for x in input().split(', ')]

prev = [None] * len(sequence)
lis = [1] * len(sequence)
max_lis_idx = 0
for idx in range(len(sequence)):
    for idx2 in range(idx - 1, -1, -1):
        if sequence[idx] >= sequence[idx2] and lis[idx] <= lis[idx2] + 1:
            prev[idx] = idx2
            lis[idx] = max(lis[idx2] + 1, lis[idx])
for idx, el in enumerate(lis):
    if el > lis[max_lis_idx]:
        max_lis_idx = idx

path = deque()
idx = max_lis_idx
while idx is not None:
    path.appendleft(sequence[idx])
    idx = prev[idx]

print(*path, sep=' ')
