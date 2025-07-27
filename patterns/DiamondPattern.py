# Take input from the user for the number of rows
n = int(input("Enter row size: "))

# First half of the pattern (upright pyramid)
for i in range(1, n + 1):
    # Print spaces to center the stars
    for j in range(0, n - i):
        print(" ", end="")
    # Print stars for the current row
    for j in range(0, 2 * i - 1):
        print("*", end="")
    # Move to the next line after each row
    print()

# Second half of the pattern (inverted pyramid)
for i in range(1, n):
    # Print spaces to center the stars
    for j in range(0, i):
        print(" ", end="")
    # Print stars for the current row
    for j in range(0, 2 * (n - i) - 1):
        print("*", end="")
    # Move to the next line after each row
    print()

"""
output

Enter row size: 6

     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
"""
