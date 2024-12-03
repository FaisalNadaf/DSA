# Initial array to be sorted
arr = [3, 5, 6, 0, 9, 4, 1, 7, 8, 2]
print("Before sorting:", arr)

# Function to swap two elements in the array
def swap(arr, i, j):
    """
    Swap two elements in an array using a temporary variable.
    
    Parameters:
    arr (list): The array containing the elements.
    i (int): Index of the first element.
    j (int): Index of the second element.
    """
    temp = arr[i]       # Step 2: Save arr[i] in a temporary variable
    arr[i] = arr[j]     # Step 3: Assign arr[j] to arr[i]
    arr[j] = temp       # Step 4: Assign the temporary value to arr[j]


# Function to sort an array using the Bubble Sort algorithm
def sort(arr):
    """
    Sort the given array in ascending order using the Bubble Sort algorithm.
    
    Parameters:
    arr (list): The array to be sorted.
    """
    # Outer loop: Perform len(arr) - 1 passes
    for i in range(len(arr) - 1):
        # Inner loop: Compare adjacent elements in the unsorted portion
        for j in range(len(arr) - 1 - i):  # Reduce range as the largest elements are sorted
            if arr[j] > arr[j + 1]:  # Compare two adjacent elements
                swap(arr, j, j + 1)  # Swap them if they are in the wrong order
    # Print the sorted array
    print("After sorting:", arr)

# Call the sort function to sort the array
sort(arr)


""""
output

Before sorting: [3, 5, 6, 0, 9, 4, 1, 7, 8, 2]
After sorting: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"""