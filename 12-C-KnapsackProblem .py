"""
Solve the 0/1 knapsack problem using dynamic programming.
Max Value
Example: Weights: [2, 3, 4, 5], Values: [3, 4, 5, 6], Capacity: 5 → Output: 7
"""

def knapsack(weights, values, capacity, kanpsackContent = None, entry = None):

    if entry == len(weights)-1:
        maxVal = 0
        val=0
        for item in kanpsackContent:
            val = sum(item[2])
            if val > maxVal:
                maxVal = val

        return maxVal
    
    if kanpsackContent is None:
        kanpsackContent = []
        entry = 1
        for i in range(len(weights)):
            if capacity - weights[i] >= 0:
                kanpsackContent.append([ [i], [weights[i]] , [values[i]] ])
                
    else:
        entry += 1
        for item in range(len(kanpsackContent)):
            for i in range(len(weights)):
            

                if i not in kanpsackContent[item][0] and sum(kanpsackContent[item][1]) + weights[i] <= capacity:
                    
                    kanpsackContent[item][0].append(i)
                    kanpsackContent[item][1].append(weights[i])
                    kanpsackContent[item][2].append(values[i])
                

    

    return knapsack(weights, values, capacity, kanpsackContent, entry)