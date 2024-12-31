def Find_Subsets(str, ans, i):
    # Base case: If we have reached the end of the string
    if i == len(str):
        # If the accumulated answer is an empty string, print "null"
        if ans == "":
            print("null")
        else:
            # Otherwise, print the accumulated answer
            print(ans)
        return
    
    # Recursive case: Include the current character in the subset
    a = ans + str[i]
    Find_Subsets(str, a, i + 1)
    
    # Recursive case: Exclude the current character from the subset
    Find_Subsets(str, ans, i + 1)

# Initial call to the function with the string "abc", an empty answer, and starting index 0
str = "abc"
Find_Subsets(str, "", 0)

# Dry run:
# Initial call: Find_Subsets("abc", "", 0)
# 1. Include 'a': Find_Subsets("abc", "a", 1)
#    1.1 Include 'b': Find_Subsets("abc", "ab", 2)
#        1.1.1 Include 'c': Find_Subsets("abc", "abc", 3) -> prints "abc"
#        1.1.2 Exclude 'c': Find_Subsets("abc", "ab", 3) -> prints "ab"
#    1.2 Exclude 'b': Find_Subsets("abc", "a", 2)
#        1.2.1 Include 'c': Find_Subsets("abc", "ac", 3) -> prints "ac"
#        1.2.2 Exclude 'c': Find_Subsets("abc", "a", 3) -> prints "a"
# 2. Exclude 'a': Find_Subsets("abc", "", 1)
#    2.1 Include 'b': Find_Subsets("abc", "b", 2)
#        2.1.1 Include 'c': Find_Subsets("abc", "bc", 3) -> prints "bc"
#        2.1.2 Exclude 'c': Find_Subsets("abc", "b", 3) -> prints "b"
#    2.2 Exclude 'b': Find_Subsets("abc", "", 2)
#        2.2.1 Include 'c': Find_Subsets("abc", "c", 3) -> prints "c"
#        2.2.2 Exclude 'c': Find_Subsets("abc", "", 3) -> prints "null"
