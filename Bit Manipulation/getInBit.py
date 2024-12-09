# Function to get the value of the ith bit of an integer n
def GetIthBit(n, i):
    # Create a bitmask with the ith bit set to 1
    bitMask = 1 << i
    # Perform bitwise AND between n and the bitmask to check the value of the ith bit
    if n & bitMask == 0:
        print(0)  # The ith bit is 0
    else:
        print(1)  # The ith bit is 1

# Example usage: Get the 2nd bit (indexing starts from 0) of the number 10
GetIthBit(10, 2)

# Example usage: Get the 4th bit (indexing starts from 0) of the number 90
GetIthBit(90, 4)
