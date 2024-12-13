# Function to calculate x to the power n using optimized recursion
def Print_x_to_the_power_n_Optimized(x, n):
    # Base case: any number to the power of 0 is 1
    if n == 0:
        return 1
    
    # Recursive step: calculate x^(n/2)
    halfPower = Print_x_to_the_power_n_Optimized(x, n // 2)  # Using integer division for n/2

    # Square the result of x^(n/2) to get x^n for even powers
    global halfPowerSqr  # Declare a global variable to store the squared result
    halfPowerSqr = halfPower * halfPower

    # If n is odd, multiply the result by x to adjust for the odd exponent
    if n % 2 != 0:
        halfPowerSqr = x * halfPowerSqr

    # Return the final result
    return halfPowerSqr

# Testing the function with x=2 and n=10
print(Print_x_to_the_power_n_Optimized(2, 10))
