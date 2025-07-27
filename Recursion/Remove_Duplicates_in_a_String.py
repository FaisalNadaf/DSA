# Function to remove duplicates in a string recursively
def Remove_Duplicates_in_a_String(string, newStr, arr, idx):
    # Base case: If the index reaches the length of the string, print the result
    if idx == len(string):  
        print(newStr)
        return

    
    # Get the current character
    currChar = string[idx]  

    # Check if the character has already been included in the result
    if arr[ord(currChar) - ord('a')]:  # Convert the character to its respective array index
        # If the character is already added, move to the next index
        Remove_Duplicates_in_a_String(string, newStr, arr, idx + 1)
    else:
        # If the character is not added, mark it as seen and add to newStr
        arr[ord(currChar) - ord('a')] = True
        # Append the current character to newStr
        Remove_Duplicates_in_a_String(string, newStr + currChar, arr, idx + 1)  

# Initialize an array to keep track of seen characters
arr = [False] * 26 

# Test the function with a string
Remove_Duplicates_in_a_String("faaaissaalll", "", arr, 0)
