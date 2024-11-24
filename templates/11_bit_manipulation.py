"""
LeetCode Questions
191 - Number of 1 bits
190 - Reverse bits
268 - Missing number
371 - Sum of two integers
338 - Counting bits
"""

"""
Useful bitwise operators for LeetCode
"""

def binary_operators():
    return {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "NOT": ~a, # ~a = -a-1 in python
        "Left Shift (a << b)": a << b,  # left shift 'a' by 'b' bits
        "Right Shift (a >> b)": a >> b,  # right shift 'a' by 'b' bits
        "Mask": a & 1 # gives you the least significant bit of a
    }