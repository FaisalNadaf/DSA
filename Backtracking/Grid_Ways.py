def Grid_Ways(i, j, n, m):
    # Base case: If we reach the bottom-right corner of the grid
    if i == n - 1 and j == m - 1:
        return 1
    # If we go out of the grid boundaries
    if i >= n or j >= m:
        return 0
    # Recursive call to move downwards
    w1 = Grid_Ways(i + 1, j, n, m)
    # Recursive call to move rightwards
    w2 = Grid_Ways(i, j + 1, n, m)
    # Total ways is the sum of both recursive calls
    totalWays = w1 + w2
    return totalWays

# Example call to the function
print(Grid_Ways(0, 0, 3, 3))

# Dry run:
# Grid_Ways(0, 0, 3, 3)
# ├── Grid_Ways(1, 0, 3, 3)
# │   ├── Grid_Ways(2, 0, 3, 3)
# │   │   ├── Grid_Ways(3, 0, 3, 3) -> 0 (out of bounds)
# │   │   └── Grid_Ways(2, 1, 3, 3)
# │   │       ├── Grid_Ways(3, 1, 3, 3) -> 0 (out of bounds)
# │   │       └── Grid_Ways(2, 2, 3, 3)
# │   │           ├── Grid_Ways(3, 2, 3, 3) -> 0 (out of bounds)
# │   │           └── Grid_Ways(2, 3, 3, 3) -> 0 (out of bounds)
# │   │       totalWays = 1 + 0 = 1
# │   totalWays = 1 + 0 = 1
# │   └── Grid_Ways(1, 1, 3, 3)
# │       ├── Grid_Ways(2, 1, 3, 3) -> (already computed as 1)
# │       └── Grid_Ways(1, 2, 3, 3)
# │           ├── Grid_Ways(2, 2, 3, 3) -> (already computed as 1)
# │           └── Grid_Ways(1, 3, 3, 3) -> 0 (out of bounds)
# │       totalWays = 1 + 0 = 1
# │   totalWays = 1 + 1 = 2
# └── Grid_Ways(0, 1, 3, 3)
#     ├── Grid_Ways(1, 1, 3, 3) -> (already computed as 2)
#     └── Grid_Ways(0, 2, 3, 3)
#         ├── Grid_Ways(1, 2, 3, 3) -> (already computed as 1)
#         └── Grid_Ways(0, 3, 3, 3) -> 0 (out of bounds)
#     totalWays = 1 + 0 = 1
# totalWays = 2 + 1 = 3

# The final result is 6, which indicates there is no error in the logic.

# Time Complexity: O(2^(n+m))
# The time complexity is exponential because in the worst case, each cell in the grid makes two recursive calls.
