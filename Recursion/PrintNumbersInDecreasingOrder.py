# Function to print numbers in decreasing order using recursion
def PrintNumbersInDecreasingOrder(n):
    # Base case: If n is 1, print 1 and return
    if n == 1:
        print(n, end=" , ")
        return
    # Print the current number followed by a comma
    print(n, end=" , ")
    # Recursive case: Call the function with (n-1) to print the next number
    PrintNumbersInDecreasingOrder(n - 1)

# Call the function with input 20 and print numbers in decreasing order
PrintNumbersInDecreasingOrder(20)
