# Merge Sort Function
def Merge_sort(arr, si, ei):
    # Base case: If the starting index is greater than or equal to the ending index, the array is already sorted
    if si >= ei:
        return

    # Calculate the middle index
    mid = si + (ei - si) // 2  # Use integer division for mid to avoid type errors

    # Recursively sort the left half
    Merge_sort(arr, si, mid)

    # Recursively sort the right half
    Merge_sort(arr, mid + 1, ei)

    # Merge the sorted halves
    merge(arr, si, ei, mid)


# Function to merge two sorted halves of the array
def merge(arr, si, ei, mid):
    # Temporary list to store the merged array
    temp = []

    # Initialize pointers for the two halves
    i = si       # Pointer for the left half
    j = mid + 1  # Pointer for the right half

    # Compare elements from both halves and add the smaller one to temp
    while i <= mid and j <= ei:
        if arr[i] < arr[j]:
            temp.append(arr[i])  # Add element from left half
            i += 1               # Move the left pointer
        else:
            temp.append(arr[j])  # Add element from right half
            j += 1               # Move the right pointer

    # Add remaining elements from the left half (if any)
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Add remaining elements from the right half (if any)
    while j <= ei:
        temp.append(arr[j])
        j += 1

    # Copy the sorted elements back into the original array
    for k in range(len(temp)):
        arr[si + k] = temp[k]  # Overwrite original array with sorted elements


# Driver Code
arr = [6, 7, 3, 6, 1, 2, 4, 6, 9, 0, 8, 8]  # Example input array
si = 0  # Starting index of the array
ei = len(arr) - 1  # Ending index of the array

# Call the Merge_sort function
Merge_sort(arr, si, ei)

# Print the sorted array
for i in range(len(arr)):
    print(arr[i],end=" , ")



# DRY RUN TREE (Input: arr = [6, 7, 3, 6, 1, 2, 4, 6, 9, 0, 8, 8])

# STEP 1: Initial division (splitting the array recursively)

# [6, 7, 3, 6, 1, 2, 4, 6, 9, 0, 8, 8]
# │
# │
# ├── Left: [6, 7, 3, 6, 1, 2]
# │   ├── Left: [6, 7, 3]
# │   │   ├── Left: [6, 7]
# │   │   │   ├── [6]
# │   │   │   └── [7]
# │   │   │   └── Merge: [6, 7]
# │   │   └── Right: [3]
# │   │   └── Merge: [3, 6, 7]
# │   └── Right: [6, 1, 2]
# │   │    ├── Left: [6]
# │   │    └── Right: [1, 2]
# │   │    │    ├── [1]
# │   │    │    └── [2]
# │   │    │    └── Merge: [1, 2]
# │   │    └── Merge: [1, 2, 6]
# │   └── Merge: [1, 2, 3, 6, 6, 7]
# │
# │
# ├── Right: [4, 6, 9, 0, 8, 8]
# │   ├── Left: [4, 6, 9]
# │   │   ├── Left: [4, 6]
# │   │   │   ├── [4]
# │   │   │   └── [6]
# │   │   │   └── Merge: [4, 6]
# │   │   └── Right: [9]
# │   │   └── Merge: [4, 6, 9]
# │   └── Right: [0, 8, 8]
# │   │    ├── Left: [0]
# │   │    └── Right: [8, 8]
# │   │    │    ├── [8]
# │   │    │    └── [8]
# │   │    │    └── Merge: [8, 8]
# │   │    └── Merge: [0, 8, 8]
# │   └── Merge: [0, 4, 6, 8, 8, 9]
# │
# │
# │ STEP 2: Final merge
# └── Merge: [0, 1, 2, 3, 4, 6, 6, 6, 7, 8, 8, 9]

# # Final Output:
# [0, 1, 2, 3, 4, 6, 6, 6, 7, 8, 8, 9]
