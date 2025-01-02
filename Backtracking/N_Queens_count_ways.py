def isSafe(board, row, col):
    # Function to check if it's safe to place a queen at board[row][col]

    # Check column
    for i in range(row, -1, -1):
        if board[i][col] == "Q":
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == "Q":
            return False

    return True


def placeQueenInRow(board, row, count):
    # Function to place queens row by row
    if row == len(board):
        # If all queens are placed, increment the count
        count[0] += 1
        return

    for i in range(0, len(board)):
        if isSafe(board, row, i):
            # Place queen at board[row][i]
            board[row][i] = "Q"
            # Recur to place queen in next row
            placeQueenInRow(board, row + 1, count)
            # Backtrack and remove queen from board[row][i]
            board[row][i] = "X"


def N_Queens_all_ways(count):
    # Main function to solve N-Queens problem
    n = 4  # Size of the board (4*4)
    board = [["X" for _ in range(n)] for _ in range(n)]  # Initialize the board with 'X'
    placeQueenInRow(board, 0, count)  # Start placing queens from the first row

count = [0]
N_Queens_all_ways(count)
print("Total ways of placing queen is =", count[0])



# Dry Run Tree:
# Start with an empty 4x4 board
# Place queen in row 0, column 0
# ├── Place queen in row 1, column 1
# │   ├── Place queen in row 2, column 2 (not safe)
# │   ├── Place queen in row 2, column 3
# │   │   ├── Place queen in row 3, column 0
# │   │   │   ├── All queens placed, count = 1
# │   │   └── Backtrack
# │   └── Backtrack
# ├── Place queen in row 1, column 2
# │   ├── Place queen in row 2, column 0
# │   │   ├── Place queen in row 3, column 3
# │   │   │   ├── All queens placed, count = 2
# │   │   └── Backtrack
# │   └── Backtrack
# ├── Place queen in row 1, column 3
# │   ├── Place queen in row 2, column 0
# │   │   ├── Place queen in row 3, column 2
# │   │   │   ├── All queens placed, count = 3
# │   │   └── Backtrack
# │   ├── Place queen in row 2, column 1
# │   │   ├── Place queen in row 3, column 2 (not safe)
# │   │   ├── Place queen in row 3, column 3 (not safe)
# │   │   └── Backtrack
# │   └── Backtrack
# └── Backtrack
# Repeat similar steps for placing queen in row 0, columns 1, 2, and 3
# Total ways of placing queens = 2
