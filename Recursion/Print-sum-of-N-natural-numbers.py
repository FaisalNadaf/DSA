# Function to calculate the sum of the first n natural numbers using recursion
def Print_sum_of_N_natural_numbers(n):
    # Base case: If n is 0, the sum is 0
    if n == 0:
        return 0
    # Recursive case: Add n to the sum of the first (n-1) natural numbers
    return n + Print_sum_of_N_natural_numbers(n - 1)

# Call the function with input 10 and print the result
print(Print_sum_of_N_natural_numbers(10))  # Expected output is 55 (1+2+3+...+10)
