# Take input from the user for the number of rows
n = int(input("Enter row size: "))

# Loop to generate each row of the pattern
for i in range(0, n):
    # Print spaces to center-align the hollow square
    for j in range(0, n - i):
        print(end=" ")
    # Loop to generate the hollow square pattern
    for j in range(0, n):
        # Print '*' for the borders of the square (first/last row, first/last column)
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        # Print spaces for the hollow part inside the square
        else:
            print(" ", end="")
    # Move to the next line after completing the row
    print()

"""
Output example

Enter row size: 5

     *****
    *   *
   *   *
  *   *
 *****
"""
