"""
Compute the factorial of a number n.

Example: Input: 5 → Output: 120
"""


def fact(x):
    if x == 0 or x == 1:
        return 1
    
    return x * fact(x-1)


