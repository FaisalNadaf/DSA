arr = [1, 2, 3, 4, 5, 6, 7, 8, 4, 9]  # The array in which we need to find the last occurrence of the key

def Last_Occurrence(arr, key, idx):
    # Base case: If we've reached the end of the array (idx == len(arr)), return -1.
    # This means the key hasn't been found yet in the remaining part of the array.
    if idx == len(arr):
        return -1
    
    # Recursively search the next element in the array.
    # isFound stores the result of the recursive call, which is the last occurrence
    # found in the remaining part of the array (from idx+1 onward).
    isFound = Last_Occurrence(arr, key, idx + 1)
    
    # If the key is not found in the remaining elements (isFound == -1) and the current element
    # is equal to the key, then the current index is the last occurrence of the key.
    if isFound == -1 and arr[idx] == key:
        return idx

    # Otherwise, return the result of the recursive call (either -1 or the index of the last occurrence).
    return isFound

# Starting the search from index 0
result = Last_Occurrence(arr, 4, 0)

# Output the result: the index of the last occurrence of the key.
# In this case, it should print 8, since 4 last appears at index 8 in the array.
print(result)
