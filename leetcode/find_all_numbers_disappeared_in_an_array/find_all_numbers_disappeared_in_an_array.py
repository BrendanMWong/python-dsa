# Set solution O(n) time, O(n) space

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        nums_set = set(nums)
        for target in range(1, len(nums) + 1):
            if target not in nums_set:
                output.append(target)
        return output
    
# Solution with O(n) time, O(1) space, sign marking technique

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Mark numbers as seen by flipping sign
        for num in nums:
            index = abs(num) - 1  # map number to index
            if nums[index] > 0:
                nums[index] *= -1
        
        # Collect numbers whose positions were never marked
        missing = []
        for i in range(n):
            if nums[i] > 0:
                missing.append(i + 1)  # missing number is index + 1
        
        return missing
