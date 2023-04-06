rolls, cals = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rolls)]

counter = 0

for r in range(rolls-1):
    for c in range(cals-1):
        if matrix[r][c] == matrix[r+1][c] == matrix[r][c+1] == matrix[r+1][c+1]:
            counter += 1

print(counter)
