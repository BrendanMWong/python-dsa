# Binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        middle = len(nums) // 2
        right = len(nums)

        while left < right:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
            middle = left + (right - left) // 2
        return left