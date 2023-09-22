rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

primary = sum([matrix[i][i] for i in range(rows)])
secondary = sum([matrix[i][rows - i - 1] for i in range(rows)])

print(abs(primary - secondary))
