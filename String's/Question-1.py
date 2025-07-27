# Q - You are given a string containing lower-case english alphabets. You need to perform the following operation as many times as possible:
# Take the first occurrence of each alphabet if it exists and remove it from the string. Eventually the string becomes empty.

# For example, let's say the string is "ababcba".
# In the first move, we need to remove the first occurrence of each character 'a', 'b' and 'c'. It becomes
# "ababeba" → "abba"
# Again, we repeat unless the string becomes empty
# "abba" → "ba"
# "ba"→""
# Find the last non-empty value for the string.

# Example 1:
# Input:s="ababcba"
# Output: "ba"
# Explanation: ababcba -> abba -> ba -> 6637


# CODE :

a = "ababcab"
b = ""
c = ""
x=""
while(len(a) != 0):
    x=a
    for i in a:
        if i not in b:
            b+=i
        else:
            c+=i
    a=c
    b=""
    c=""

print(x)