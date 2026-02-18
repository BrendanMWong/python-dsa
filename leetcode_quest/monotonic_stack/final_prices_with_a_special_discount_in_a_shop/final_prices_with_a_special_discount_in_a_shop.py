class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        output = prices[:]
        for index in range(len(prices)):
            while stack != [] and prices[stack[-1]] >= prices[index]:
                popped_index = stack.pop()
                output[popped_index] -= prices[index]
            stack.append(index)
        return output