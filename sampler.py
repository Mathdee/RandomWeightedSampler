#sampler.py
"""
How I coded this: 
The Goal: Picks an item at random in a list where each item is assigned a weight.
The Challenge: The items with higher weights have a higher probability of being selected
relative to their weight. 
Probability equation: P(item) = weight(item) / total_weight

Solution:
-Found total weight by summing all weights in the list and building a prefix sum array.
-Generated a random integer n between 0 and the total weight.
-If n is in the range of the prefix sum array, return the item at the index of the prefix sum array.
-Binary search is used to find the index of the item in the prefix sum array.
"""

import random
from typing import List, Tuple, Any

class RandomWeightedSampler:

    def __init__(self, items: List[Tuple[Any, float]]):
        if not items:
            raise ValueError("Item list can't be empty!!")

        self.items = []
        self.pre_sums = []

        total_weight = 0.0
        for item, weight in items:
            if weight <= 0:
                raise ValueError("Weight must be positive!!")
            self.items.append(item)
            total_weight += weight
            self.pre_sums.append(total_weight)
        if total_weight <=0:
            raise ValueError("Total weight must be positive!!")
        self.total_weight = total_weight

    def binarySearch(self, target:float)->int: 
        #A lower bound binary search is used to find smallest index i where pre_sums[i] >= randomly generated integer.
        #Time Complexity: O(log n)
        left, right = 0, len(self.pre_sums)-1
        while left <= right:
            mid = (left + right) // 2
            if self.pre_sums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def sample(self) -> Any:
        #returns one item with a probability proportional to its weight.
        n = random.random()* self.total_weight
        index = self.binarySearch(n)
        return self.items[index]
    
    def sample_multiple(self, k:int) -> List[Any]:
        #returns multiple items with probabilities proportional to weights.
        return [self.sample() for _ in range(k)]



    


