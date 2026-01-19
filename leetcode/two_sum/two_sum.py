from typing import List

# Brute force solution for the Two Sum problem, O(n^2) time complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Optimal solution for the Two Sum problem using a dictionary (hash map), O(n) time complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number (key) should point to index (value) in dict
        data = {}
        
        for index in range(len(nums)):
            # current number + needed number = target
            # needed number = target - current number
            current_number = nums[index]
            needed_number = target - current_number

            # search if needed number is in the dict, return if true
            if needed_number in data:
                return [data[needed_number], index]

            # add new key value pair to dict
            data[nums[index]] = index
            
        return []