# Function to search for a key in a sorted and rotated array
def Sorted_Rotated_Array(arr, key, si, ei):
    # Base Case: If the start index exceeds the end index, the key is not found
    if si > ei:
        return -1

    # Calculate the middle index
    mid = si + (ei - si) // 2

    # If the middle element is the key, return its index
    if arr[mid] == key:
        return mid

    # Check if the left half (si to mid) is sorted
    if arr[si] <= arr[mid]:
        # If the key lies within the sorted left half
        if arr[si] <= key <= arr[mid]:
            # Recursively search in the left half
            return Sorted_Rotated_Array(arr, key, si, mid - 1)
        else:
            # Otherwise, search in the right half
            return Sorted_Rotated_Array(arr, key, mid + 1, ei)
    else:
        # If the right half (mid to ei) is sorted
        if arr[mid] <= key <= arr[ei]:
            # If the key lies within the sorted right half
            return Sorted_Rotated_Array(arr, key, mid + 1, ei)
        else:
            # Otherwise, search in the left half
            return Sorted_Rotated_Array(arr, key, si, mid - 1)


# Driver Code
arr = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]  # Input array
key = 0  # Key to search for
si = 0  # Start index
ei = len(arr) - 1  # End index

# Call the function and print the result
result = Sorted_Rotated_Array(arr, key, si, ei)
print(f"Index of {key}: {result}")



# [4, 5, 6, 7, 8, 9, 0, 1, 2, 3], si=0, ei=9
# ├── Calculate mid = (0 + 9) // 2 = 4
# │   ├── arr[mid] = 8 != key
# │   ├── Left half [4, 5, 6, 7, 8] is sorted
# │   └── Key (0) is not in range [4, 8]
# │       └── Recur to right half: si=5, ei=9
# │
# ├── [9, 0, 1, 2, 3], si=5, ei=9
# │   ├── Calculate mid = (5 + 9) // 2 = 7
# │   ├── arr[mid] = 1 != key
# │   ├── Left half [9, 0, 1] is not sorted
# │   └── Right half [1, 2, 3] is sorted
# │       └── Key (0) is in range [0, 1]
# │       └── Recur to left half: si=5, ei=6
# │
# ├── [9, 0], si=5, ei=6
# │   ├── Calculate mid = (5 + 6) // 2 = 5
# │   ├── arr[mid] = 9 != key
# │   ├── Left half [9] is sorted
# │   └── Key (0) is not in range [9, 9]
# │       └── Recur to right half: si=6, ei=6
# │
# └── [0], si=6, ei=6
#     ├── Calculate mid = (6 + 6) // 2 = 6
#     ├── arr[mid] = 0 == key
#     └── Return index 6

