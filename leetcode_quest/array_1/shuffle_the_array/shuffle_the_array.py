class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        firstpointer = 0
        secondpointer = n
        while firstpointer < n:
            output.append(nums[firstpointer])
            firstpointer += 1
            output.append(nums[secondpointer])
            secondpointer += 1
        return output