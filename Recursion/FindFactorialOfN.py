# Function to calculate the factorial of a number n
def FindFactorialOfN(n):
    # Base case: If n is 0, return 1 (since 0! = 1)
    if n == 0:
        return 1
    # Recursive case: Multiply n by the factorial of (n-1)
    return n * FindFactorialOfN(n - 1)

# Call the function with the input 5 and print the result
print(FindFactorialOfN(5))  # Expected output is 120 (5! = 5*4*3*2*1)
