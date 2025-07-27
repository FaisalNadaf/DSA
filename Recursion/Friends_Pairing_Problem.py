def Friends_Pairing_Problem(n):
    # Base case: 
    # If there's only 1 friend, they can only stay single (1 way).
    # If there are 2 friends, they can either stay single or pair up (2 ways).
    if n == 1 or n == 2:
        return n
    
    # Recursive case:
    # Choice 1: The nth friend stays single. 
    # This leaves the problem with (n-1) friends.
    fnm1 = Friends_Pairing_Problem(n - 1)

    # Choice 2: The nth friend pairs up with any one of the (n-1) friends.
    # This leaves the problem with (n-2) friends, and there are (n-1) ways to pair.
    fnm2 = Friends_Pairing_Problem(n - 2)
    fnm2Ways = (n - 1) * fnm2

    # Total ways = single ways + pairing ways
    return fnm1 + fnm2Ways

# Example: Find the number of ways to pair or keep 6 friends single
print(Friends_Pairing_Problem(6))
