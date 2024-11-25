"""
Transpose a given matrix (swap rows and columns).

Example: Input: [[1, 2], [3, 4]] → Output: [[1, 3], [2, 4]]
"""

def Transpose(x):
    for i in range(0,len(x)):
        j = 0
        while j < len(x[i]) and (i-j>0):
            temp = x[i][j]
            x[i][j] = x[j][i]
            x[j][i] = temp
            j += 1

    return x

