r, c = [int(x) for x in input().split(", ")]

matrix = [[int(s) for s in input().split()] for _ in range(r)]

for c in range(c):
    col_sum = 0
    for rol in range(len(matrix)):
        col_sum += matrix[rol][c]
    print(col_sum)
