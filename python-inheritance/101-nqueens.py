import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, n):
    if row == n:
        # Print the solution
        for i in range(n):
            print("".join(["Q" if cell == 1 else "." for cell in board[i]]))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen and move to the next row
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n)
            # Backtrack
            board[row][col] = 0

def solve_nqueens(n):
    # Initialize the chessboard
    board = [[0] * n for _ in range(n)]
    
    # Start solving from the first row
    solve_nqueens_util(board, 0, n)

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command-line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater than or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    solve_nqueens(N)
