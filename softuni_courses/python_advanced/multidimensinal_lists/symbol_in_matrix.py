matrix = [[i for i in input()] for _ in range(int(input()))]
searching = input()

found = False

for r in range(len(matrix)):
    for c in range(len(matrix)):

        if matrix[r][c] == searching:
            print(f"({r}, {c})")
            exit()

print(f"{searching} does not occur in the matrix")
