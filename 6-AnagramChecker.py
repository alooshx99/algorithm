"""
Write a function that checks if two strings are anagrams of each other.

Example: Input: "listen", "silent" → Output: True
"""

def checker(x):
    if len(x[0]) != len(x[1]):
        return False

    for i in x[0]:
        if i in x[1]:
            x[1] = x[1].replace( i ,'', 1 )

    if len(x[1]) == 0:
        return True

    else: return False

    

    



