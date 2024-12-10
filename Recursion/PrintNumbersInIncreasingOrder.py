# Function to print numbers in increasing order using recursion
def PrintNumbersInIncreasingOrder(n):
    # Base case: If n is 1, print 1 and return
    if n == 1:
        print(n, end=" , ")
        return
    # Recursive case: First call the function with (n-1), printing smaller numbers first
    PrintNumbersInIncreasingOrder(n - 1)
    # After the recursion call, print the current number
    print(n, end=" , ")

# Call the function with input 20 and print numbers in increasing order
PrintNumbersInIncreasingOrder(20)
