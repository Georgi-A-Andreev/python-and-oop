from collections import deque

string = input().split()

max_seq = [1] * len(string)
prev = [None] * len(string)
max_current_seq = 0
for idx, el in enumerate(string):
    for idx2 in range(idx - 1, -1, -1):
        if len(el) > len(string[idx2]) and max_seq[idx2] + 1 >= max_current_seq:
            max_current_seq = max_seq[idx2] + 1
            prev[idx] = idx2
            max_seq[idx] = max_current_seq

path = deque()
last_index = max_seq.index(max(max_seq))

while last_index is not None:
    path.appendleft(string[last_index])
    last_index = prev[last_index]

print(*path, sep=' ')

