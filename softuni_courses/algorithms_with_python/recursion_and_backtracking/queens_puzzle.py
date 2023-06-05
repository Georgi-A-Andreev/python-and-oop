def queens(matrix, row):
    if row == 8:
        print(' '.join(matrix))
        print()
        return

    for col in range(8):
        pass


field = []
[field.append(['-'] * 8) for i in range(8)]

queens(field, 0)
