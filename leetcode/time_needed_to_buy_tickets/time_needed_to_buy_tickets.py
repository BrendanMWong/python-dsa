# Using a queue is a trap

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for index in range(len(tickets)):
            if index <= k:
                count += min(tickets[index], tickets[k])
            else:
                count += min(tickets[index], tickets[k] - 1)
        return count
