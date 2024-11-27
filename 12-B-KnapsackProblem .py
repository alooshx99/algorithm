"""
Solve the 0/1 knapsack problem using dynamic programming.
Sorting over values
Example: Weights: [2, 3, 4, 5], Values: [3, 4, 5, 6], Capacity: 5 → Output: 7
"""

def knapsack(weights, values, capacity):
    arr =[]
    subArr = []
    for i in range(len(weights)):
        subArr.append(values[i])
        subArr.append(weights[i])
        arr.append(subArr)
        subArr = []

    arr.sort(reverse=True)

    knapsackValue = 0

    while capacity > 0:
        for item in arr:
            if capacity - item[1] < 0:
                continue
            else:
                capacity -= item[1]
                knapsackValue += item[0]




    return knapsackValue
