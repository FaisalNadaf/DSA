# Initial array to be sorted
arr = [3, 5, 6, 0, 9, 4, 1, 7, 8, 2]  # A list of unsorted integers
print("Before sorting:", arr)  # Print the array before sorting

# Function to sort an array using the Insertion Sort algorithm
def sort(arr):
    # Loop through each element in the array, starting from the second one
    for i in range(1, len(arr)):  
        curr = arr[i]  # Store the current element
        prev = i - 1  # Index of the previous element
        
        # Shift elements of the sorted portion of the array that are larger than 'curr' one position ahead
        while prev >= 0 and arr[prev] > curr:  # Continue until the correct position for 'curr' is found
            arr[prev + 1] = arr[prev]  # Shift the larger element forward
            prev -= 1  # Move to the previous element
        
        # Place 'curr' in its correct position
        arr[prev + 1] = curr  

# Call the sort function to sort the array
sort(arr)

# Print the sorted array
print("After sorting:", arr)  # Output the sorted array
