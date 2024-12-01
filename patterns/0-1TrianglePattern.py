# Prompt the user to input a value for n
n = int(input("Enter n value: "))

# Outer loop to iterate through rows from 0 to n-1
for i in range(0, n):
    # Inner loop to iterate through columns from 0 to i-1
    for j in range(0, i):
        # Calculate the sum of the current row and column indices
        x = i + j
        # Check if the sum is odd
        if x % 2 == 1:
            print(1, end="")  # Print 1 without a newline if the sum is odd
        else:
            print(0, end="")  # Print 0 without a newline if the sum is even
    # Move to the next line after each row
    print()




"""
output

Enter n value: 6

1
01
101
0101
10101

"""