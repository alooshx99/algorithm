"""
Given a list of intervals, merge overlapping intervals.

Example: Input: [[1, 3], [2, 6], [8, 10], [15, 18]] → Output: [[1, 6], [8, 10], [15, 18]]
"""

def mergeIntervals(x):
    x.sort()
    arr = []
    preItem = x[0][0]

    for i in range(len(x)):
        for j in range(2):
           if preItem > x[i][j]:
               arr.pop()
               continue
           preItem = x[i][j]
           arr.append(x[i][j])
        
    final = [arr[i:i+2] for i in range(0, len(arr), 2)]
            

    return final



