class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        min_val = min(s)
        longest = 0
        for num in s:
            if num - 1 not in s:
                count = 1
                current = num
                while current + 1 in s:
                    count += 1
                    current += 1
                longest = max(longest, count)
        return longest