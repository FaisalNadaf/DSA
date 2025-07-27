# Function to solve the tiling problem using recursion
def Tiling_Problem(n):
    # Base cases:
    # If n == 0 (no tiles needed), there is 1 way to arrange them (do nothing).
    # If n == 1 (only 1 unit of floor), there is 1 way to place the tile vertically.
    if n == 0 or n == 1:
        return 1

    # Recursive step:
    # fnm1: Number of ways to tile the floor by placing the first tile vertically (reduces problem to n-1).
    fnm1 = Tiling_Problem(n - 1)

    # fnm2: Number of ways to tile the floor by placing the first two tiles horizontally (reduces problem to n-2).
    fnm2 = Tiling_Problem(n - 2)

    # Total number of ways to tile the floor is the sum of the above two possibilities
    totalWays = fnm1 + fnm2

    # Return the total number of ways
    return totalWays

# Testing the function with n=3 (length of the floor is 3)
print(Tiling_Problem(3))
