rolls, cols = [int(el) for el in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rolls)]

max_sum = float('-inf')
max_matrix = []

for r in range(rolls-2):
    for c in range(cols-2):
        first_row = matrix[r][c:c+3]
        second_row = matrix[r+1][c:c+3]
        third_row = matrix[r+2][c:c+3]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*i) for i in max_matrix]
