from collections import deque

string = input().split()

prev = [-1] * len(string)
lis = [1] * len(string)
max_seq_idx = 0
max_seq = 0
for idx in range(len(string)):
    for idx2 in range(idx - 1, -1, -1):
        if len(string[idx]) > len(string[idx2]):
            if lis[idx2] + 1 >= lis[idx]:
                prev[idx] = idx2
                lis[idx] = max(lis[idx2] + 1, lis[idx])
                if lis[idx] > max_seq:
                    max_seq = lis[idx]
                    max_seq_idx = idx

path = deque()
el = max_seq_idx
while el != -1:
    path.appendleft(string[el])
    el = prev[el]

print(*path, sep=' ')