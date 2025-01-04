def Grid_Ways(n, m):    
    # Calculate the total number of steps needed to reach the bottom-right corner
    v = (n - 1) + (m - 1)
    
    # Calculate factorial of (n-1)
    x = fact(n - 1)
    
    # Calculate factorial of (m-1)
    y = fact(m - 1)
    
    # Calculate factorial of the total steps
    i = fact(v)
    
    # Calculate the number of ways using the formula:
    # (n-1 + m-1)! / [(n-1)! * (m-1)!]
    a = x * y
    return i // a

# Helper function to calculate factorial of a number
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

# Example usage: Calculate the number of ways to reach the bottom-right corner of a 3x3 grid
print(Grid_Ways(3, 3))

# Dry run example for Grid_Ways(3, 3):
# n = 3, m = 3
# v = (3-1) + (3-1) = 4
# x = fact(3-1) = fact(2) = 2 * 1 = 2
# y = fact(3-1) = fact(2) = 2 * 1 = 2
# i = fact(4) = 4 * 3 * 2 * 1 = 24
# a = x * y = 2 * 2 = 4
# result = i // a = 24 // 4 = 6
# So, Grid_Ways(3, 3) returns 6

# Time complexity analysis:
# The time complexity of the fact function is O(n) because it makes n recursive calls.
# Since the fact function is called three times in Grid_Ways, the overall time complexity is O(n + m + (n+m-2)).
# Simplifying, the time complexity is O(n + m).
