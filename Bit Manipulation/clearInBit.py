# Function to clear (set to 0) the ith bit of an integer n
def clearIthBit(n, i):
    # Create a bitmask with all bits set to 1 except the ith bit, which is set to 0
    bitMask = ~(1 << i)
    # Perform bitwise AND between n and the bitmask to clear the ith bit of n
    print(n & bitMask)

# Example usage: clear the 1st bit (indexing starts from 0) of the number 10
clearIthBit(10, 1)

# Example usage: clear the 4th bit (indexing starts from 0) of the number 25
clearIthBit(25, 4)
