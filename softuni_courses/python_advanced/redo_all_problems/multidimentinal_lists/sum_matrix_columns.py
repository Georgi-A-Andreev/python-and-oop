rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for c in range(cols):
    summ = 0
    for r in range(rows):
        summ += matrix[r][c]
    print(summ)

