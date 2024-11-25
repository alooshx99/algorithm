"""
Find the maximum number in a list without using the max() function.

Example: Input: [4, 2, 9, 7, 5] → Output: 9
"""

def Maximum(x):
    max = x[0]

    for i in range(0,len(x)):
        if x[i] > max:
            max = x[i]

    return max


