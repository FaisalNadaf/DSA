arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # The array in which we need to find the first occurrence of the key

def First_Occurrence(arr, key, idx):
    # Base case: If we have checked all elements and didn't find the key, return -1.
    # If we reach the last element and haven't found the key yet, return -1 to indicate key is not present.
    if idx == len(arr):
        return -1
    
    # If the current element is equal to the key, return the current index.
    # This is the first occurrence of the key in the array.
    if arr[idx] == key:
        return idx
    
    # Recursively check the next element.
    # Move to the next index (idx + 1) and repeat the search.
    return First_Occurrence(arr, key, idx + 1)

# Starting the search from index 0
result = First_Occurrence(arr, 4, 0)

# Output the result: the index of the first occurrence of the key.
# In this case, it should print 3, since 4 is at index 3 in the array.
print(result)
