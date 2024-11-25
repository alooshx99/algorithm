"""
Generate the first n numbers in the Fibonacci sequence.

Example: Input: 5 → Output: [0, 1, 1, 2, 3]
"""

def fibo(x):
   listOfNums = [0]
   
   if x == 0 or x == 1:
       return listOfNums
   
   listOfNums.append(1)

   for i in range(2,x):
        listOfNums.append( ( listOfNums[i-1] + listOfNums[i-2] ) )
        
        
   
   return listOfNums
   



