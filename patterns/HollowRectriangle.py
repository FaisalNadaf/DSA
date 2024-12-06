# Take input from the user for the number of rows (this will be a square pattern)
n = int(input("Enter row size: "))

# Loop through each row (from 0 to n-1)
for i in range(0, n):
    
    # Loop through each column (from 0 to n-1)
    for j in range(0, n):
        
        # Check if the current position is on the boundary (first or last row, first or last column)
        if(i == 0 or i == n-1 or j == 0 or j == n-1):
            # Print "*" for boundary positions
            print("*", end="")
        else:
            # Print space for positions inside the boundary
            print(end=" ")
    
    # After completing the columns for the current row, move to the next line
    print()
