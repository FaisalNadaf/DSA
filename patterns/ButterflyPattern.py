# Take input from the user for the number of rows
n = int(input("Enter row size: "))

# First half of the pattern
for i in range(0, n):
    # Print increasing '*' in the first section
    for j in range(0, i):
        print("*", end="")
    # Print spaces between the two '*' sections
    for j in range(0, 2 * (n - i)):
        print(" ", end="")
    # Print increasing '*' in the second section
    for j in range(0, i):
        print("*", end="")
    # Move to the next line after each row
    print()

# Second half of the pattern (in reverse order)
for i in range(n, 0, -1):
    # Print decreasing '*' in the first section
    for j in range(0, i):
        print("*", end="")
    # Print spaces between the two '*' sections
    for j in range(0, 2 * (n - i)):
        print(" ", end="")
    # Print decreasing '*' in the second section
    for j in range(0, i):
        print("*", end="")
    # Move to the next line after each row
    print()



"""
output

Enter row size: 6

*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

"""