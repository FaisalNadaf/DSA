def changeArr(arr, i, val):
    # Base case: If the index i reaches the length of the array, print the array and return
    if i == len(arr):
        print(arr)
        return
    
    # Set the current index of the array to the current value
    arr[i] = val
    
    # Recursive call: Increment the index and value
    changeArr(arr, i + 1, val + 1)
    
    # Backtrack step: Decrement the current index of the array by 2
    arr[i] -= 2

# Initialize an array of size 5 with all elements set to 0
arr = [0] * 5 

# Call the changeArr function starting from index 0 and initial value 1
changeArr(arr, 0, 1)

# Print the final state of the array after all recursive calls and backtracking
print(arr)

# Dry Run Tree:
# changeArr(arr, 0, 1)
# ├── arr[0] = 1
# ├── changeArr(arr, 1, 2)
# │   ├── arr[1] = 2
# │   ├── changeArr(arr, 2, 3)
# │   │   ├── arr[2] = 3
# │   │   ├── changeArr(arr, 3, 4)
# │   │   │   ├── arr[3] = 4
# │   │   │   ├── changeArr(arr, 4, 5)
# │   │   │   │   ├── arr[4] = 5
# │   │   │   │   ├── changeArr(arr, 5, 6)
# │   │   │   │   │   └── print([1, 2, 3, 4, 5])
# │   │   │   │   └── arr[4] -= 2 -> arr[4] = 3
# │   │   │   └── arr[3] -= 2 -> arr[3] = 2
# │   │   └── arr[2] -= 2 -> arr[2] = 1
# │   └── arr[1] -= 2 -> arr[1] = 0
# └── arr[0] -= 2 -> arr[0] = -1

# Final array state: [-1, 0, 1, 2, 3]