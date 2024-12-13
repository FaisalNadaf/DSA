# Function to calculate x to the power n using simple recursion
def Print_x_to_the_power_n(x, n):
    # Base case: any number raised to the power of 0 is 1
    if n == 0:
        return 1

    # Recursive step: multiply x by the result of the function with a reduced exponent
    return x * Print_x_to_the_power_n(x, n - 1)

# Testing the function with x=2 and n=10
print(Print_x_to_the_power_n(2, 10))

