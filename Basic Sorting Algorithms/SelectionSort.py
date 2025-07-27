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

# Function to sort an array using the Selection Sort algorithm
def sort(arr):
    """
    Sort the given array in ascending order using the Selection Sort algorithm.
    
    Parameters:
    arr (list): The array to be sorted.
    """
    # Outer loop: Traverse the array from the beginning to the second-to-last element
    for i in range(0, len(arr) - 1):
        minPos = i  # Assume the current position `i` is the smallest element
        # Inner loop: Compare the current element with the remaining elements
        for j in range(i + 1, len(arr)):
            # If we find a smaller element, update the index of the smallest element
            if arr[minPos] > arr[j]:
                minPos = j
        # Swap the smallest element found with the element at the current position
        swap(arr, i, minPos)

# Call the sort function to sort the array
sort(arr)

# Print the sorted array
print("After sorting:", arr)
