matrix = [[int(x) for x in input().split(", ")]for _ in range(int(input()))]


primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[r][len(matrix)-r-1] for r in range(len(matrix))]

print(f"Primary diagonal: {', '.join(str(i) for i in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(i) for i in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
