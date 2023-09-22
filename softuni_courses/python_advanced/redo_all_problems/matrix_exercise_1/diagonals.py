matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
p_d = []
s_d = []
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if row == col:
            p_d.append(matrix[row][col])

for row in range(len(matrix)):
    for col in range(len(matrix) - 1, -1, -1):
        if row + col == len(matrix) - 1:
            s_d.append(matrix[row][col])

print(f'Primary diagonal: {", ".join(str(x) for x in p_d)}. Sum: {sum(p_d)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in s_d)}. Sum: {sum(s_d)}')
