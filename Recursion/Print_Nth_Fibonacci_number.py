# Function to calculate the nth Fibonacci number using recursion
def Print_Nth_Fibonacci_number(n):
    # Base case: The 0th Fibonacci number is 0
    if n == 0:
        return 0
    # Base case: The 1st Fibonacci number is 1
    if n == 1:
        return 1
    # Recursive case: Calculate the (n-1)th and (n-2)th Fibonacci numbers
    fib1 = Print_Nth_Fibonacci_number(n - 1)  # Recursive call for (n-1)th Fibonacci
    fib2 = Print_Nth_Fibonacci_number(n - 2)  # Recursive call for (n-2)th Fibonacci
    # Combine the results to get the nth Fibonacci number
    return fib1 + fib2

# Calculate and print the 10th Fibonacci number
print(Print_Nth_Fibonacci_number(10))  # Expected output: 55
