def Binary_Strings_Problem(n, lastPlace, string):
    # Base case: If n becomes 0, print the binary string and return
    if n == 0:
        print(string)
        return
    
    # Recursive case: Add "0" to the string and reduce the problem size by 1
    Binary_Strings_Problem(n - 1, 0, string + "0")
    
    # If the last placed character was "0", we can add "1"
    if lastPlace == 0:
        Binary_Strings_Problem(n - 1, 1, string + "1")

# Initial call to generate all binary strings of length 3 with no consecutive 1's
Binary_Strings_Problem(3, 0, "")
