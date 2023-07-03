def can_place_queen(board, row, col, rows, cols, left_d, right_d):
    if row in rows:
        return False
    if col in cols:
        return False
    if row + col in left_d:
        return False
    if row - col in right_d:
        return False
    return True


def set_queen(board, row, col, rows, cols, left_d, right_d):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_d.add(row + col)
    right_d.add(row - col)


def remove_queen(board, row, col, rows, cols, left_d, right_d):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_d.remove(row + col)
    right_d.remove(row - col)


def print_board(board):
    for i in board:
        print(*i, sep=' ')
    print()


def put_queens(board, row, col, rows, cols, left_d, right_d):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(board, row, col, rows, cols, left_d, right_d):
            set_queen(board, row, col, rows, cols, left_d, right_d)
            put_queens(board, row + 1, col, rows, cols, left_d, right_d)
            remove_queen(board, row, col, rows, cols, left_d, right_d)


board = [['-'] * 8 for _ in range(8)]
put_queens(board, 0, 0, set(), set(), set(), set())
