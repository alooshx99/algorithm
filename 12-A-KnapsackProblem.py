"""
Solve the 0/1 knapsack problem using dynamic programming.
Sorting over average (values to weights)
Example: Weights: [2, 3, 4, 5], Values: [3, 4, 5, 6], Capacity: 5 → Output: 6
"""

def knapsack(weights, values, capacity):
    arr =[]
    subArr = []
    for i in range(len(weights)):
        subArr.append(values[i]/weights[i])
        subArr.append(values[i])
        subArr.append(weights[i])
        arr.append(subArr)
        subArr = []

    arr.sort()

    knapsackValue = 0

    while capacity > 0:
        for item in arr:
            if capacity - item[2] < 0:
                continue
            else:
                capacity -= item[2]
                knapsackValue += item[1]




    return knapsackValue