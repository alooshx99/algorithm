"""
Implement the binary search algorithm to find an element in a sorted list.

Example: Input: [1, 3, 5, 7, 9], Target: 5 => Output: Index 2
"""


def BinaryS(x, target):

    mid = len(x)//2
    
    if x[mid] == target:
        return mid
    
    firstHalf = x[:mid]
    secondHalf = x[mid+1:]

    if target < x[mid]:
        return BinaryS(firstHalf, target) 

    else: return mid + 1 + BinaryS(secondHalf, target)


