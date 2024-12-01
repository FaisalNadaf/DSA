# Take input from the user for the number of rows
n = int(input("Enter row size: "))

# Initialize a variable `a` to store the current number to be printed
a = 1

# Outer loop: Iterates through each row
for i in range(0, n):

    # Inner loop: Controls the number of elements printed in the current row
    for j in range(0, i):

        print(a, end="")  # Print the current value of `a` without moving to a new line

        a += 1  # Increment `a` for the next number
        
    print()  # Move to the next line after printing all numbers in the current row




"""
output

Enter n value: 6

Enter row size: 6

1
23
456
78910
1112131415

"""