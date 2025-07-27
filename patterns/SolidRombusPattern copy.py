# Take input from the user for the number of rows
n = int(input("Enter row size: "))

# Loop to generate each row of the pattern
for i in range(0, n):
    # Print spaces to align the rows diagonally
    for j in range(0, n - i):
        print(" ", end="")
    # Print '*' n times for each row
    for j in range(0, n):
        print("*", end="")
    # Move to the next line after completing the row
    print()

"""
Output example

Enter row size: 5

     *****
    *****
   *****
  *****
 *****
"""
