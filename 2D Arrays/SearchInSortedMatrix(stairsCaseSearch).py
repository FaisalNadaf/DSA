# Initialize the 2D array (matrix) with the given values
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

# Starting position (row 0, last column of the matrix)
row = 0
col = len(arr[0]) - 1  # Get the index of the last column
key = 17  # The key to search for in the matrix

# Function to search for the key in the matrix
def sort(arr, key, row, col):
    # While within the matrix bounds, search for the key
    while(row < len(arr) - 1 and col >= 0):
        
        # If the current element matches the key, print its position and return True
        if(arr[row][col] == key):
            print("key found at", row, col)
            return True
        
        # If the key is smaller than the current element, move left (decrease column)
        elif(key < arr[row][col]):
            col -= 1
        
        # If the key is larger, move down (increase row)
        else:
            row += 1
    
    # If the key was not found, print a message and return False
    print("key not found")
    return False

# Call the function to search for the key in the matrix
sort(arr, key, row, col)


# O(n+m)


"""
output 

key found at 3 1
"""