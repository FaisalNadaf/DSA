arr = [1,2,3,4,5,6,7,8,9]  # The array to check if it's sorted

def Check_if_array_is_sorted_or_not(arr, idx):
    # Base case: If the index is the last element, return True.
    # If we reach the last element, no more elements are left to compare,
    # and we've checked that all previous elements are in order.
    if idx == len(arr) - 1:
        return True
    
    # If the current element is greater than the next element, return False.
    # This means the array is not sorted in increasing order.
    if arr[idx] > arr[idx + 1]:
        return False
    
    # Recursively check the next element.
    # We move to the next index (idx + 1) and repeat the process.
    return Check_if_array_is_sorted_or_not(arr, idx + 1)

# Starting the check from index 0
result = Check_if_array_is_sorted_or_not(arr, 0)

# Output the result: True if the array is sorted, False if it is not
print(result)
