"""
Write a program to find all prime numbers less than n.

Example: Input: 10 → Output: [2, 3, 5, 7]
"""

def findPrime(x):
    arr = [2,3,5,7] #or we can just let arr = [2] and start the loop from 3
    for i in range(10,x):
        for j in arr:
            if i%j == 0:
                break
            elif j == arr[-1]:
                arr.append(i)
        


    return arr



print(findPrime(200))