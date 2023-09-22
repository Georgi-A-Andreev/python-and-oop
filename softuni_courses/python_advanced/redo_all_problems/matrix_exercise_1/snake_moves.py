from collections import deque

rows, cols = [int(x) for x in input().split()]

string = deque(input())

matrix = []
for _ in range(rows):
    matrix.append([''] * cols)

for r in range(rows):
    for c in range(cols):
        char = string.popleft()
        matrix[r][c] = char
        string.append(char)

for idx, el in enumerate(matrix):
    if idx % 2 != 0:
        print(*el[::-1], sep='')
    else:
        print(*el, sep='')
