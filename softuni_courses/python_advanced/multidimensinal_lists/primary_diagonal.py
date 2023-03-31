matrix = [[int(x) for x in input().split()]for _ in range(int(input()))]

p_d_sum = 0

for i in range(len(matrix)):
    p_d_sum += matrix[i][i]

print(p_d_sum)
