rows = int(input())

matrix = [list(input()) for _ in range(rows)]

removed_knights = 0

directions = [
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (-1, -2),
    (1, -2)
]

while True:
    best_knight = []
    best_knight_counter = 0

    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == 'K':
                current_attacks = 0
                for i in directions:
                    if 0 <= row + i[0] < rows and 0 <= col + i[1] < rows and matrix[row+i[0]][col+i[1]] == 'K':
                        current_attacks += 1
                if current_attacks > best_knight_counter:
                    best_knight_counter = current_attacks
                    best_knight = [row, col]
    if best_knight_counter:
        matrix[best_knight[0]][best_knight[1]] = '0'
        removed_knights += 1
    else:
        break
print(removed_knights)


