
"""
Determine if a given string is a palindrome (reads the same forwards and backwards).

Example: Input: "radar" → Output: True
"""

import math

def checker(x):
    for i in range(0,math.ceil(len(x)/2)):
        if x[i] != x[len(x)-i-1]:
            return False
        
        if (len(x) % 2 !=0) and (i+1 == math.ceil(len(x)/2)):
            break
    
    return True

