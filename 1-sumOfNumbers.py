"""
Write a program that takes a list of numbers as input and returns their sum.

Example: Input: [1, 2, 3, 4, 5] → Output: 15
"""


def sumFunction(x):
    if len(x) == 0:
        return 0
    return int(x.pop(0))+sumFunction(x)

