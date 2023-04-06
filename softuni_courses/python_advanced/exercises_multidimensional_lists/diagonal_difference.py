matrix = [[int(el) for el in input().split()]for _ in range(int(input()))]

primary = [matrix[i][i] for i in range(len(matrix))]
secondary = [matrix[i][len(matrix)-i-1] for i in range(len(matrix))]

print(abs(sum(primary) - sum(secondary)))
