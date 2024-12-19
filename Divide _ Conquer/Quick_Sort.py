# Quick Sort Function
def Quick_Sort(arr, si, ei):
    # Base case: If the starting index is greater than or equal to the ending index, return
    if si >= ei:
        return
    
    # Partition the array and get the pivot index
    pIdx = partition(arr, si, ei)
    
    # Recursively sort the left subarray
    Quick_Sort(arr, si, pIdx - 1)
    
    # Recursively sort the right subarray
    Quick_Sort(arr, pIdx + 1, ei)

# Partition Function
def partition(arr, si, ei):
    # Set the pivot as the element at the ending index
    pivot = arr[ei]
    i = si - 1  # Pointer for the smaller element

    # Iterate through the array to place elements smaller than or equal to pivot
    for j in range(si, ei):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot element in its correct position
    i += 1
    arr[i], arr[ei] = arr[ei], arr[i]
    return i

# Driver Code
arr = [6, 7, 3, 6, 1, 2, 4, 6, 9, 0, 8, 8]  # Input array
si = 0  # Starting index
ei = len(arr) - 1  # Ending index

# Call the Quick_Sort function
Quick_Sort(arr, si, ei)

# Print the sorted array
for i in range(len(arr)):
    print(arr[i], end=", ")




# DRY RUN TREE (Input: arr = [6, 7, 3, 6, 1, 2, 4, 6, 9, 0, 8, 8])

# STEP 1: Initial call to Quick_Sort(arr, si=0, ei=11)
# [6, 7, 3, 6, 1, 2, 4, 6, 9, 0, 8, 8]
# ├── Partition with pivot=8 (ei=11)
# │   ├── Swapping to ensure elements <= pivot:
# │   │   Result: [6, 7, 3, 6, 1, 2, 4, 6, 0, 8, 8, 9]
# │   └── Pivot placed at position 10 (pIdx=10)
# │
# ├── Left Subarray: [6, 7, 3, 6, 1, 2, 4, 6, 0, 8]
# │   ├── Partition with pivot=8 (ei=9)
# │   │   ├── Swapping to ensure elements <= pivot:
# │   │   │   Result: [6, 7, 3, 6, 1, 2, 4, 6, 0, 8]
# │   │   └── Pivot placed at position 9 (pIdx=9)
# │   │
# │   ├── Left Subarray: [6, 7, 3, 6, 1, 2, 4, 6, 0]
# │   │   ├── Partition with pivot=0 (ei=8)
# │   │   │   ├── Swapping to ensure elements <= pivot:
# │   │   │   │   Result: [0, 7, 3, 6, 1, 2, 4, 6, 6, 8]
# │   │   │   └── Pivot placed at position 0 (pIdx=0)
# │   │   │
# │   │   └── Right Subarray: [7, 3, 6, 1, 2, 4, 6, 6]
# │   │       ├── Partition with pivot=6 (ei=8)
# │   │       │   ├── Swapping to ensure elements <= pivot:
# │   │       │   │   Result: [0, 3, 1, 2, 4, 6, 6, 6, 7, 8]
# │   │       │   └── Pivot placed at position 5 (pIdx=5)
# │   │       │
# │   │       ├── Left Subarray: [3, 1, 2, 4]
# │   │       │   ├── Partition with pivot=4 (ei=4)
# │   │       │   │   ├── Swapping to ensure elements <= pivot:
# │   │       │   │   │   Result: [0, 1, 2, 3, 4, 6, 6, 6, 7, 8]
# │   │       │   │   └── Pivot placed at position 4 (pIdx=4)
# │   │       │   │
# │   │       │   └── Left Subarray: [1, 2, 3]
# │   │       │       ├── Partition with pivot=3 (ei=3)
# │   │       │       │   ├── Swapping to ensure elements <= pivot:
# │   │       │       │   │   Result: [0, 1, 2, 3, 4, 6, 6, 6, 7, 8]
# │   │       │       │   └── Pivot placed at position 3 (pIdx=3)
# │   │       │       │
# │   │       │       └── Subarray sorted as: [1, 2, 3]
# │   │       │
# │   │       └── Subarray sorted as: [1, 2, 3, 4]
# │   │
# │   └── Subarray sorted as: [0, 1, 2, 3, 4, 6, 6, 6, 7, 8]
# │
# └── Right Subarray: [9]
#     ├── Sorted as: [9]

# Final Merge:
# [0, 1, 2, 3, 4, 6, 6, 6, 7, 8, 8, 9]

