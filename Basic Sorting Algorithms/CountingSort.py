# Initialize an array with unsorted integers
arr = [6, 5, 4, 6, 5, 8, 9, 1, 2, 3, 5, 3, 2, 3, 7, 6, 4, 1]

# Function to sort the array using the Counting Sort algorithm
def counting_sort(arr):
    if not arr:  # Handle edge case where the array is empty
        return arr

    # Step 1: Find the largest element in the array to determine the size of the count array
    largest = max(arr)

    # Step 2: Initialize the count array with zeros
    # The size of the count array is (largest + 1) to account for all possible values from 0 to 'largest'
    count = [0] * (largest + 1)

    # Step 3: Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1  # Increment the count for the element `num`

    # Step 4: Reconstruct the sorted array using the count array
    sorted_index = 0  # Start index for updating the input array
    for i in range(len(count)):  # Iterate through each index in the count array
        while count[i] > 0:  # If the count of element `i` is greater than 0
            arr[sorted_index] = i  # Place the element `i` at the current sorted index
            sorted_index += 1  # Move to the next index in the sorted array
            count[i] -= 1  # Decrement the count of element `i`

# Print the array before sorting
print("Before sorting:", arr)

# Call the counting_sort function to sort the array
counting_sort(arr)

# Print the array after sorting
print("After sorting:", arr)
