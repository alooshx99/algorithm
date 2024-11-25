"""
Given a sentence, find the longest word.

Example: Input: "The quick brown fox" → Output: "quick
"""

def longestWord(x):
    x = x.split()
    max = x[0]
    for i in x:
        if len(i) > len(max):
            max = i

    return max


