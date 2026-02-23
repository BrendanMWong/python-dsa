class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicates = set()
        duplicate_value = None
        missing_value = None
        for element in nums:
            if element in duplicates:
                duplicate_value = element
            else:
                duplicates.add(element)

        for number in range(1, len(nums) + 1):
            if number not in duplicates:
                missing_value = number
                break
        
        return [duplicate_value, missing_value]