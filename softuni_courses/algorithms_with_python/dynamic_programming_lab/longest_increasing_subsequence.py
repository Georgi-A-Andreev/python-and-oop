from collections import deque

n = [int(x) for x in input().split(', ')]

prev = [None] * len(n)
subsequence = [1] * len(n)
biggest_so_far = 0
for idx, el in enumerate(n):
    for i in range(idx - 1, -1, -1):
        if el >= n[i]:
            if subsequence[idx] <= subsequence[i] + 1:
                subsequence[idx] = subsequence[i] + 1
                prev[idx] = i

for idx, i in enumerate(subsequence):
    if i > subsequence[biggest_so_far]:
        biggest_so_far = idx

result = deque()

idx = biggest_so_far
while idx is not None:
    result.appendleft(n[idx])
    idx = prev[idx]

print(*result, sep=' ')
