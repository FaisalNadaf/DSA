# Problem Statement
# Chef has a string S. He is happy if the string contains any contiguous substring of length ≥ 3 where all characters are vowels (a, e, i, o, u).

# Output:

# "HAPPY" if such a substring exists.

# "SAD" otherwise.

# Examples
# Example 1
# Input: "aeiou"
# Explanation:

# Substrings of length ≥ 3: "aei", "eio", "iou", "aeio", "eiou", "aeiou"

# All are made of vowels → HAPPY
# Output: "HAPPY"

# Example 2
# Input: "abxy"
# Explanation:

# No substring of length ≥ 3 has all vowels → SAD
# Output: "SAD"




str ="bjskiseeon "

vovels="aeiou"
a=""
for i in str:
    if(i in vovels ):
        a+="1"
    else:
        a+="0"

print(a)

if( "111" in a):
    a="HAPPY"
else:
    a="SAD"

print(a)