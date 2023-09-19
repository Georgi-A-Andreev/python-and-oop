rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

summ = 0

for el in matrix:
    summ += sum(el)

print(summ)
print(matrix)
