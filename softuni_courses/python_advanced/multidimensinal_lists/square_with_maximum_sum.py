r, c = [int(i) for i in input().split(", ")]

result = []
max_sum = 0

matrix = [[int(x) for x in input().split(", ")]for _ in range(r)]

for rol in range(r - 1):
    for col in range(c - 1):
        if matrix[rol][col] + matrix[rol + 1][col] + matrix[rol][col + 1] + matrix[rol + 1][col + 1] > max_sum:
            max_sum = matrix[rol][col] + matrix[rol + 1][col] + matrix[rol][col + 1] + matrix[rol + 1][col + 1]
            result = [[matrix[rol][col], matrix[rol][col + 1]],[matrix[rol+1][col], matrix[rol+1][col+1]]]

[print(*i) for i in result]
print(max_sum)
