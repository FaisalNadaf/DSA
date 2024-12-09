# Function to set (turn to 1) the ith bit of an integer n
def SetIthBit(n, i):
    # Create a bitmask with the ith bit set to 1
    bitMask = 1 << i
    # Perform bitwise OR between n and the bitmask to set the ith bit of n
    print(n | bitMask)

# Example usage: set the 2nd bit (indexing starts from 0) of the number 10
SetIthBit(10, 2)

# Example usage: set the 4th bit (indexing starts from 0) of the number 25
SetIthBit(25, 4)
