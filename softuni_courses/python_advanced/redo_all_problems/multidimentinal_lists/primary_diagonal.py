rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

d_sum = 0
for r in range(rows):
    d_sum += matrix[r][r]

print(d_sum)
