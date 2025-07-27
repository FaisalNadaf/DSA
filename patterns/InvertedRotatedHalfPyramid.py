# Prompt the user to input a value for n
n = int(input("Enter n value: "))

# Outer loop: Iterates through each row
for i in range(0, n):

    # Inner loop: Prints numbers for each row, decreasing as i increases
    for j in range(0, n - i):
        
        print(j, end="")  # Print the current value of j without moving to the next line

    print()  # Print a newline after completing each row



"""
output

Enter n value: 6
012345
01234
0123
012
01
0

"""