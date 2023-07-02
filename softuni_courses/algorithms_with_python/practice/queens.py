def is_safe(board, row, col):
    # Check if a queen can be placed at the given row and column
    # without attacking any other queen on the board
    for i in range(col):
        if board[i] == row or board[i] - row == i - col or board[i] - row == col - i:
            return False
    return True


def solve_queens(board, col, solutions):
    # Base case: If all queens are placed, add the current solution to the list
    if col == len(board):
        solutions.append(board[:])
        return

    # Try placing a queen in each row of the current column
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[col] = row
            solve_queens(board, col + 1, solutions)
            board[col] = -1


def print_solutions(solutions):
    # Print all solutions
    for i, solution in enumerate(solutions):
        for row in range(len(solution)):
            print(" ".join("*" if solution[row] == col else "-" for col in range(len(solution))))
        print()


# Initialize an 8x8 chess board represented by a list
board = [-1] * 8

# List to store all solutions
solutions = []

# Solve the problem
solve_queens(board, 0, solutions)

# Print the solutions
print_solutions(solutions)
