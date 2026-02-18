class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highest_count = 0
        for element in nums:
            if element == 1:
                count += 1
                highest_count = max(highest_count, count)
            else:
                count = 0
        return highest_count