def printBoard(board):
    # Function to print the current state of the board
    print("---------------BOARD---------------")
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col):
    # Function to check if it's safe to place a queen at board[row][col]

    # Check if there's a queen in the same column
    for i in range(row, -1, -1):
        if board[i][col] == "Q":
            return False

    # Check if there's a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check if there's a queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == "Q":
            return False

    return True


def placeQueenInRow(board, row):
    # Function to place queens row by row
    if row == len(board):
        return True

    for i in range(0, len(board)):
        if isSafe(board, row, i):
            # Place queen at board[row][i]
            board[row][i] = "Q"
            # Recur to place queen in the next row
            if placeQueenInRow(board, row + 1):
                return True
            
            # Backtrack and remove queen from board[row][i]
            board[row][i] = "X"
    return False


def N_Queens_all_ways():
    # Main function to solve the N-Queens problem
    n = 4  # Size of the board (4x4)
    board = [["X" for _ in range(n)] for _ in range(n)]  # Initialize the board with 'X'
    if placeQueenInRow(board, 0):
        print("Solution is possible")
        printBoard(board)
    else:
        print("Solution is not possible")


N_Queens_all_ways()

# Dry Run Tree:
# Initial call: placeQueenInRow(board, 0)
# 
# placeQueenInRow(board, 0)
# ├── placeQueenInRow(board, 1) [Q at (0, 0)]
# │   ├── placeQueenInRow(board, 2) [Q at (1, 2)]
# │   │   ├── placeQueenInRow(board, 3) [Q at (2, 1)]
# │   │   │   ├── placeQueenInRow(board, 4) [Q at (3, 3)]
# │   │   │   │   └── Solution found, return True
# │   │   │   └── Backtrack, remove Q from (3, 3)
# │   │   ├── Backtrack, remove Q from (2, 1)
# │   │   ├── placeQueenInRow(board, 3) [Q at (2, 3)]
# │   │   │   └── Backtrack, remove Q from (2, 3)
# │   ├── Backtrack, remove Q from (1, 2)
# │   ├── placeQueenInRow(board, 2) [Q at (1, 3)]
# │   │   └── Backtrack, remove Q from (1, 3)
# ├── Backtrack, remove Q from (0, 0)
# ├── placeQueenInRow(board, 1) [Q at (0, 1)]
# │   └── Backtrack, remove Q from (0, 1)
# ├── placeQueenInRow(board, 1) [Q at (0, 2)]
# │   └── Backtrack, remove Q from (0, 2)
# ├── placeQueenInRow(board, 1) [Q at (0, 3)]
# │   └── Backtrack, remove Q from (0, 3)
# 
# The tree continues until a solution is found or all possibilities are exhausted.
