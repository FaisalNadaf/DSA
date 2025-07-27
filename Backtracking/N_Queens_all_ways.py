def printBoard(board):
    # Function to print the current state of the board
    print("-----------------------BOARD----------------------------")
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            print(board[i][j], end=" ")
        print()


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


def placeQueenInRow(board, row):
    # Function to place queens row by row
    if row == len(board):
        # If all queens are placed, print the board
        printBoard(board)
        return

    for i in range(0, len(board)):
        if isSafe(board, row, i):
            # Place queen at board[row][i]
            board[row][i] = "Q"
            # Recur to place queen in next row
            placeQueenInRow(board, row + 1)
            # Backtrack and remove queen from board[row][i]
            board[row][i] = "X"


def N_Queens_all_ways():
    # Main function to solve N-Queens problem
    n = 4  # Size of the board (4x4)
    board = [["X" for _ in range(n)] for _ in range(n)]  # Initialize the board with 'X'
    placeQueenInRow(board, 0)  # Start placing queens from the first row


N_Queens_all_ways()


# Dry Run Tree (Visual Representation):
# Start with an empty 4x4 board
# ┌───────────────┐
# │ Place queen in row 0 │
# └───────────────┘
#     ├── Try placing queen at (0, 0)
#     │   ┌───────────────┐
#     │   │ Place queen in row 1 │
#     │   └───────────────┘
#     │       ├── Try placing queen at (1, 0) -> Not safe
#     │       ├── Try placing queen at (1, 1) -> Not safe
#     │       ├── Try placing queen at (1, 2)
#     │       │   ┌───────────────┐
#     │       │   │ Place queen in row 2 │
#     │       │   └───────────────┘
#     │       │       ├── Try placing queen at (2, 0) -> Not safe
#     │       │       ├── Try placing queen at (2, 1) -> Not safe
#     │       │       ├── Try placing queen at (2, 2) -> Not safe
#     │       │       ├── Try placing queen at (2, 3)
#     │       │       │   ┌───────────────┐
#     │       │       │   │ Place queen in row 3 │
#     │       │       │   └───────────────┘
#     │       │       │       ├── Try placing queen at (3, 0) -> Not safe
#     │       │       │       ├── Try placing queen at (3, 1)
#     │       │       │       │   ┌───────────────┐
#     │       │       │       │   │ Place queen in row 4 -> Solution found │
#     │       │       │       │   └───────────────┘
#     │       │       │       ├── Backtrack from (3, 1)
#     │       │       │       ├── Try placing queen at (3, 2) -> Not safe
#     │       │       │       ├── Try placing queen at (3, 3) -> Not safe
#     │       │       │       └── Backtrack from (2, 3)
#     │       │       └── Backtrack from (1, 2)
#     │       ├── Try placing queen at (1, 3)
#     │       │   ┌───────────────┐
#     │       │   │ Place queen in row 2 │
#     │       │   └───────────────┘
#     │       │       ├── Try placing queen at (2, 0)
#     │       │       │   ┌───────────────┐
#     │       │       │   │ Place queen in row 3 │
#     │       │       │   └───────────────┘
#     │       │       │       ├── Try placing queen at (3, 0) -> Not safe
#     │       │       │       ├── Try placing queen at (3, 1) -> Not safe
#     │       │       │       ├── Try placing queen at (3, 2)
#     │       │       │       │   ┌───────────────┐
#     │       │       │       │   │ Place queen in row 4 -> Solution found │
#     │       │       │       │   └───────────────┘
#     │       │       │       ├── Backtrack from (3, 2)
#     │       │       │       ├── Try placing queen at (3, 3) -> Not safe
#     │       │       │       └── Backtrack from (2, 0)
#     │       │       ├── Try placing queen at (2, 1) -> Not safe
#     │       │       ├── Try placing queen at (2, 2) -> Not safe
#     │       │       ├── Try placing queen at (2, 3) -> Not safe
#     │       │       └── Backtrack from (1, 3)
#     │       └── Backtrack from (0, 0)
#     ├── Try placing queen at (0, 1)
#     │   (Similar steps as above)
#     ├── Try placing queen at (0, 2)
#     │   (Similar steps as above)
#     └── Try placing queen at (0, 3)
#         (Similar steps as above)
