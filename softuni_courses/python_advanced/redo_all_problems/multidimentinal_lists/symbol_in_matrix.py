rows = int(input())

matrix = [list(input()) for _ in range(rows)]

el_to_find = input()
found = False
for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == el_to_find:
            print((r, c))
            found = True
    if found:
        break

else:
    print(f'{el_to_find} does not occur in the matrix')
