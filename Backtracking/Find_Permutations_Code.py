def Find_Permutations_Code(str, ans):
    # Base case: if the input string is empty, print the accumulated answer
    if str == "":
        print(ans)
        return
    
    # Loop through each character in the string
    for i in range(0, len(str)):
        currChar = str[i]  # Current character
        newStr = str[:i] + str[i+1:]  # New string without the current character
        # Recursive call with the new string and the current character added to the answer
        Find_Permutations_Code(newStr, ans + currChar)

# Initial call to the function with the string "abc" and an empty answer
Find_Permutations_Code("abcdefghijklmnopqrstuvwxyz", "")

# Dry run:
# Initial call: Find_Permutations_Code("abc", "")
# i = 0, currChar = 'a', newStr = "bc"
#   Recursive call: Find_Permutations_Code("bc", "a")
#   i = 0, currChar = 'b', newStr = "c"
#       Recursive call: Find_Permutations_Code("c", "ab")
#       i = 0, currChar = 'c', newStr = ""
#           Recursive call: Find_Permutations_Code("", "abc")
#           Base case reached, print "abc"
#   i = 1, currChar = 'c', newStr = "b"
#       Recursive call: Find_Permutations_Code("b", "ac")
#       i = 0, currChar = 'b', newStr = ""
#           Recursive call: Find_Permutations_Code("", "acb")
#           Base case reached, print "acb"
# i = 1, currChar = 'b', newStr = "ac"
#   Recursive call: Find_Permutations_Code("ac", "b")
#   i = 0, currChar = 'a', newStr = "c"
#       Recursive call: Find_Permutations_Code("c", "ba")
#       i = 0, currChar = 'c', newStr = ""
#           Recursive call: Find_Permutations_Code("", "bac")
#           Base case reached, print "bac"
#   i = 1, currChar = 'c', newStr = "a"
#       Recursive call: Find_Permutations_Code("a", "bc")
#       i = 0, currChar = 'a', newStr = ""
#           Recursive call: Find_Permutations_Code("", "bca")
#           Base case reached, print "bca"
# i = 2, currChar = 'c', newStr = "ab"
#   Recursive call: Find_Permutations_Code("ab", "c")
#   i = 0, currChar = 'a', newStr = "b"
#       Recursive call: Find_Permutations_Code("b", "ca")
#       i = 0, currChar = 'b', newStr = ""
#           Recursive call: Find_Permutations_Code("", "cab")
#           Base case reached, print "cab"
#   i = 1, currChar = 'b', newStr = "a"
#       Recursive call: Find_Permutations_Code("a", "cb")
#       i = 0, currChar = 'a', newStr = ""
#           Recursive call: Find_Permutations_Code("", "cba")
#           Base case reached, print "cba"