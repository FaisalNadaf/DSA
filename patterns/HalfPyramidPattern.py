# Take input from the user for the number of rows
n = int(input("Enter row size: "))

# Outer loop to iterate over each row (1 to n)
for i in range(0, n + 1):

    for j in range(0, i):
        print("*", end="")  # Print '*' without moving to the next line

    # Print a new line after completing one row
    print()


"""
output

Enter row size: 6

*
**
***
****
*****
******

"""