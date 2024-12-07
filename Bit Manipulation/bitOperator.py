# Assign values to variables
a = 4  # Binary: 0100
b = 7  # Binary: 0111

# Perform bitwise AND operation
# Result: 0100 & 0111 = 0100 (decimal: 4)
print(a & b)  # Output: 4

# Perform bitwise OR operation
# Result: 0100 | 0111 = 0111 (decimal: 7)
print(a | b)  # Output: 7

# Perform bitwise XOR operation
# Result: 0100 ^ 0111 = 0011 (decimal: 3)
print(a ^ b)  # Output: 3

# Perform bitwise NOT operation on `a`
# Result: ~0100 = -(0100 + 1) = -0101 (decimal: -5)
print(~a)  # Output: -5

# Perform left shift operation on `a` by `b` positions
# Left shift: Shift bits of `a` (0100) 7 positions to the left
# Result: 0100 << 7 = 1000000000 (binary, decimal: 512)  
#formula to calculate a*2^b
print(a << b)  # Output: 512 

# Perform right shift operation on `b` by `a` positions
# Right shift: Shift bits of `b` (0111) 4 positions to the right
# Result: 0111 >> 4 = 0 (binary, decimal: 0)
#formula to calculate a/2^b
print(b >> a)  # Output: 0
