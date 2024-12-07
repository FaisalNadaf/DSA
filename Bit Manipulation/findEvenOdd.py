# Function to check whether a number is EVEN or ODD using bitwise operations
def EvenOdd(n):
    # Initialize a bit mask with the value 1
    bitMask = 1
    # Perform bitwise AND operation between the number and the bit mask
    # Check if the result is 0 (indicating the number is even)
    if (n & bitMask == 0):  # Correct this to: (n & bitMask) == 0
        print("EVEN")  # Print EVEN if the condition is true
    else:
        print("ODD")  # Print ODD if the condition is false

# Test the function with various numbers
EvenOdd(9)    # Test case 1: ODD number
EvenOdd(289)  # Test case 2: ODD number
EvenOdd(26)   # Test case 3: EVEN number
EvenOdd(3)    # Test case 4: ODD number
