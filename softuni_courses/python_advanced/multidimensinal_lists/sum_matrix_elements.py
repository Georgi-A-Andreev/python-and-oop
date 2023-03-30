r, c = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0

for i in range(r):
    matrix.append([int(x) for x in input().split(", ")])

matrix_sum = sum([sum(i) for i in matrix])
print(matrix_sum)
print(matrix)
